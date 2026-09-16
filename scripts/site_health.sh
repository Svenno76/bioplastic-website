#!/bin/bash
# Site Health Monitor - Runs every 15 minutes
# Profile: ops | No LLM

set -euo pipefail

SITE_URL="https://bioplasticsportal.com"
WEBHOOK_URL="${ALERT_WEBHOOK:-}"
LOG_FILE="/home/jarvis/.hermes/logs/health_check_$(date +%Y%m%d).log"
DIR="/tmp/bioplastics-website"

mkdir -p "$(dirname "$LOG_FILE")"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

alert() {
    local msg="$1"
    log "ALERT: $msg"
    if [[ -n "$WEBHOOK_URL" ]]; then
        curl -s -X POST -H 'Content-type: application/json' \
            --data "{\"text\":\"🚨 BPP Health Alert: $msg\"}" \
            "$WEBHOOK_URL" >/dev/null 2>&1 || true
    fi
}

log "=== Health Check Started ==="

# 1. Site HTTP check (force IPv4 to avoid IPv6 timeout issues)
http_code=$(curl -s -4 -o /dev/null -w "%{http_code}" --max-time 10 "$SITE_URL" || echo "000")
if [[ "$http_code" != "200" ]]; then
    alert "Site returned HTTP $http_code"
else
    log "Site OK: HTTP 200"
fi

# 2. Disk usage
disk_usage=$(df -h "$DIR" | awk 'NR==2 {print $5}' | sed 's/%//')
if [[ "$disk_usage" -gt 85 ]]; then
    alert "Disk usage at ${disk_usage}%"
else
    log "Disk OK: ${disk_usage}%"
fi

# 3. Memory usage
mem_usage=$(free | awk 'NR==2 {printf "%.0f", $3*100/$2}')
if [[ "$mem_usage" -gt 90 ]]; then
    alert "Memory usage at ${mem_usage}%"
else
    log "Memory OK: ${mem_usage}%"
fi

# 4. CPU load (1-min average)
cpu_load=$(uptime | awk -F'load average:' '{print $2}' | awk '{print $1}' | sed 's/,//')
cpu_cores=$(nproc)
cpu_pct=$(echo "$cpu_load $cpu_cores" | awk '{printf "%.0f", $1/$2*100}')
if [[ "$cpu_pct" -gt 95 ]]; then
    alert "CPU load at ${cpu_pct}% (${cpu_load} on ${cpu_cores} cores)"
else
    log "CPU OK: ${cpu_pct}% (load: ${cpu_load})"
fi

# 5. Hugo build test (quick)
cd "$DIR"
if hugo --gc --minify >/dev/null 2>&1; then
    log "Hugo build OK"
else
    alert "Hugo build FAILED"
fi

# 6. Git status
if git status --porcelain | grep -q .; then
    log "Git: Uncommitted changes present"
else
    log "Git: Clean"
fi

log "=== Health Check Complete ==="
