.PHONY: verify verify-build verify-news-filter verify-no-stale

verify: verify-build verify-news-filter verify-no-stale

verify-build:
	cd /home/pi/bioplastic-website && hugo --gc --minify
	test -f /home/pi/bioplastic-website/public/index.html

verify-news-filter:
	grep -q 'data-title=' /home/pi/bioplastic-website/public/news/index.html
	grep -q 'function applyFilters' /home/pi/bioplastic-website/public/news/index.html
	grep -q 'function setFilter' /home/pi/bioplastic-website/public/news/index.html

verify-no-stale:
	! grep -q '<select' /home/pi/bioplastic-website/public/news/index.html
	! grep -q 'filterPosts(' /home/pi/bioplastic-website/public/news/index.html
	! grep -q 'filterNews(' /home/pi/bioplastic-website/public/news/index.html
