import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import { url } from "@utils/url-utils";
import type { APIContext } from "astro";
import MarkdownIt from "markdown-it";
import sanitizeHtml from "sanitize-html";
import { siteConfig } from "@/config";

const parser = new MarkdownIt();

function stripInvalidXmlChars(str: string): string {
	return str.replace(
		// biome-ignore lint/suspicious/noControlCharactersInRegex: https://www.w3.org/TR/xml/#charsets
		/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\x9F\uFDD0-\uFDEF\uFFFE\uFFFF]/g,
		"",
	);
}

export async function GET(context: APIContext) {
	// Get English posts for the English RSS feed
	const enPosts = await getCollection("posts/en", ({ data }) => {
		return import.meta.env.PROD ? data.draft !== true : true;
	});
	
	const blog = enPosts.sort((a, b) => {
		const dateA = new Date(a.data.published);
		const dateB = new Date(b.data.published);
		return dateA > dateB ? -1 : 1;
	});

	return rss({
		title: `${siteConfig.title} - English`,
		description: `${siteConfig.subtitle} - English posts`,
		site: context.site ?? "https://yunqing.org",
		items: blog.map((post) => ({
			title: post.data.title,
			pubDate: post.data.published,
			description: post.data.description || "",
			link: url(`/en/posts/${post.data.slug || post.slug}/`), // Use custom slug if available
			content: stripInvalidXmlChars(
				sanitizeHtml(parser.render(post.body), {
					allowedTags: sanitizeHtml.defaults.allowedTags.concat([
						"img",
						"video",
						"audio",
						"source",
					]),
				}),
			),
			categories: post.data.tags,
		})),
		customData: `<language>en-US</language>`,
	});
}
