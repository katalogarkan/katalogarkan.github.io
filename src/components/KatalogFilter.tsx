// src/components/KatalogFilter.tsx
import { useState } from 'react';

interface Project {
  title: string;
  description: string;
  techStack: string[];
  thumbnail: string;
  demoUrl?: string;
  repoUrl?: string;
  category: string;
  date: string; // Kita ubah jadi string agar aman saat passing data
  slug: string;
}

interface Props {
  projects: Project[];
}

export default function KatalogFilter({ projects }: Props) {
  const [search, setSearch] = useState('');
  const [category, setCategory] = useState('All');
  const [sort, setSort] = useState('newest');

  // 1. Logika Filter & Search
  const filteredProjects = projects.filter((project) => {
    const matchesSearch = 
      project.title.toLowerCase().includes(search.toLowerCase()) || 
      project.techStack.some(tech => tech.toLowerCase().includes(search.toLowerCase()));
    
    const matchesCategory = category === 'All' || project.category === category;
    
    return matchesSearch && matchesCategory;
  });

  // 2. Logika Sort
  const sortedProjects = [...filteredProjects].sort((a, b) => {
    const dateA = new Date(a.date).getTime();
    const dateB = new Date(b.date).getTime();
    return sort === 'newest' ? dateB - dateA : dateA - dateB;
  });

  return (
    <div>
      {/* Control Panel (Search, Filter, Sort) */}
      <div className="flex flex-col md:flex-row gap-4 mb-8 bg-bg-subtle p-4 rounded-lg border border-border">
        
        {/* Search */}
        <div className="relative flex-grow">
          <input 
            type="text" 
            placeholder="Search projects or tech..." 
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full px-4 py-2 pl-10 rounded-md border border-border bg-bg text-text focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary"
          />
          <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center px-3 text-text-muted">
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          </div>
        </div>

        {/* Category Filter */}
        <select 
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          className="px-4 py-2 rounded-md border border-border bg-bg text-text font-medium focus:outline-none focus:ring-2 focus:ring-primary cursor-pointer"
        >
          <option value="All">All Categories</option>
          <option value="web-app">Web App</option>
          <option value="data-engineering">Data Engineering</option>
          <option value="cloud-devops">Cloud & DevOps</option>
        </select>

        {/* Sort */}
        <select 
          value={sort}
          onChange={(e) => setSort(e.target.value)}
          className="px-4 py-2 rounded-md border border-border bg-bg text-text font-medium focus:outline-none focus:ring-2 focus:ring-primary cursor-pointer"
        >
          <option value="newest">Newest First</option>
          <option value="oldest">Oldest First</option>
        </select>
      </div>

      {/* Project Grid */}
      {sortedProjects.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {sortedProjects.map((project) => (
            <div key={project.slug} className="h-full">
              {/* Kartu Project (HTML representation agar bisa dirender React) */}
              <a href={`/katalog/${project.slug}`} className="group block bg-bg border border-border rounded-lg overflow-hidden shadow-sm hover:shadow-lg transition-all duration-200 flex flex-col h-full">
                <div className="aspect-video w-full overflow-hidden bg-gray-200 relative">
                  <img src={project.thumbnail} alt={project.title} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy" />
                  <span className="absolute top-3 right-3 bg-bg/90 backdrop-blur text-text text-xs font-medium px-2 py-1 rounded-md border border-border capitalize">
                    {project.category.replace('-', ' ')}
                  </span>
                </div>
                <div className="p-5 flex flex-col flex-grow">
                  <h3 className="text-lg font-bold text-text group-hover:text-primary transition-colors mb-2">{project.title}</h3>
                  <p className="text-sm text-text-muted mb-4 line-clamp-2 flex-grow">{project.description}</p>
                  <div className="flex flex-wrap gap-1 mb-4">
                    {project.techStack.map((tech) => (
                      <span key={tech} className="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-primary/10 text-primary">{tech}</span>
                    ))}
                  </div>
                </div>
              </a>
            </div>
          ))}
        </div>
      ) : (
        <div className="bg-bg-subtle border border-border rounded-lg p-12 text-center">
          <p className="text-text-muted text-lg">No projects found matching your criteria.</p>
          <button onClick={() => { setSearch(''); setCategory('All'); }} className="mt-4 text-primary font-medium hover:underline">Clear filters</button>
        </div>
      )}
    </div>
  );
}