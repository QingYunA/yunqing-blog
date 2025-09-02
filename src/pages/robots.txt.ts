import type { APIRoute } from "astro";

const robotsTxt = `
User-agent: *
Allow: /
Disallow: /_astro/
Disallow: /api/
Disallow: /.well-known/
Disallow: /admin/

# Allow specific crawlers
User-agent: Googlebot
Allow: /
Allow: /en/

User-agent: Bingbot
Allow: /
Allow: /en/

User-agent: Slurp
Allow: /
Allow: /en/

# Crawl-delay for less aggressive crawlers
User-agent: *
Crawl-delay: 1

# Host directive to specify the preferred domain
Host: https://yunqing.org

# Sitemaps
Sitemap: ${new URL("sitemap-index.xml", import.meta.env.SITE).href}
Sitemap: ${new URL("rss.xml", import.meta.env.SITE).href}
`.trim();

export const GET: APIRoute = () => {
	return new Response(robotsTxt, {
		headers: {
			"Content-Type": "text/plain; charset=utf-8",
		},
	});
};
