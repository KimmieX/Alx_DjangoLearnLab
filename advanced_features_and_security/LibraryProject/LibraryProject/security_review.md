# Security Review: HTTPS and Secure Redirects

## Configured Settings
- SECURE_SSL_REDIRECT: Enforces HTTPS
- HSTS: Ensures long-term HTTPS usage
- Secure Cookies: Prevents transmission over HTTP
- Secure Headers: Mitigates XSS, clickjacking, and MIME sniffing

## Deployment Notes
- SSL configured via Nginx with TLSv1.2+
- Certificates managed via Let's Encrypt

## Recommendations
- Periodically audit headers using tools like [securityheaders.com](https://securityheaders.com)
- Rotate SSL certificates regularly
