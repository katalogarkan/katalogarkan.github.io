import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const katalog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/katalog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    techStack: z.array(z.string()),
    thumbnail: z.string(),
    demoUrl: z.url().optional(),
    repoUrl: z.url().optional(),
    category: z.enum(['web-app', 'landing-page', 'api', 'mobile', 'data-engineering', 'cloud-devops']),
    featured: z.boolean().default(false),
    date: z.coerce.date(),
  }),
});

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    description: z.string(),
    category: z.enum(['tutorial', 'tips', 'notes']),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    coverImage: z.string().optional(),
  }),
});

export const collections = { katalog, blog };