.PHONY: verify verify-build verify-news-filter verify-no-stale

verify: verify-build verify-news-filter verify-no-stale

verify-build:
	cd /tmp/bioplastics-website && hugo --gc --minify
	test -f /tmp/bioplastics-website/public/index.html

verify-news-filter:
	grep -q 'data-title=' /tmp/bioplastics-website/public/news/index.html
	grep -q 'function applyFilters' /tmp/bioplastics-website/public/news/index.html
	grep -q 'function setFilter' /tmp/bioplastics-website/public/news/index.html

verify-no-stale:
	! grep -q '<select' /tmp/bioplastics-website/public/news/index.html
	! grep -q 'filterPosts(' /tmp/bioplastics-website/public/news/index.html
	! grep -q 'filterNews(' /tmp/bioplastics-website/public/news/index.html
