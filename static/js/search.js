// Context-aware search functionality with Fuse.js
(function() {
  'use strict';

  // Configuration for each section
  const sectionConfig = {
    '/news/': {
      name: 'News',
      indexUrl: '/news/index.json',
      searchKeys: ['title', 'summary', 'company', 'category'],
      threshold: 0.3,
      formatResult: formatNewsResult
    },
    '/companies/': {
      name: 'Companies',
      indexUrl: '/companies/index.json',
      searchKeys: ['title', 'description', 'headquarters', 'primary_materials'],
      threshold: 0.3,
      formatResult: formatCompanyResult
    },
    '/glossary/': {
      name: 'Glossary',
      indexUrl: '/glossary/index.json',
      searchKeys: ['title', 'summary', 'aka'],
      threshold: 0.2,
      formatResult: formatGlossaryResult
    },
    '/blog/': {
      name: 'Blog',
      indexUrl: '/blog/index.json',
      searchKeys: ['title', 'summary', 'tags'],
      threshold: 0.3,
      formatResult: formatBlogResult
    },
    '/events/': {
      name: 'Events',
      indexUrl: '/events/index.json',
      searchKeys: ['title', 'description', 'location', 'event_type'],
      threshold: 0.3,
      formatResult: formatEventResult
    }
  };

  // Cache for loaded indexes
  const indexCache = {};
  let currentSection = null;
  let currentFuse = null;
  let searchTimeout = null;

  // Initialize search on DOM ready
  document.addEventListener('DOMContentLoaded', initializeSearch);

  function initializeSearch() {
    // Detect current section from URL
    currentSection = detectCurrentSection();

    // Get DOM elements
    const searchToggle = document.getElementById('search-toggle');
    const searchCloseBtn = document.getElementById('search-close');
    const searchInput = document.getElementById('search-input');
    const searchBoxContainer = document.getElementById('search-box-container');
    const searchModal = document.getElementById('search-modal');
    const searchModalBackdrop = document.getElementById('search-modal-backdrop');
    const searchModalClose = document.getElementById('search-modal-close');

    if (!searchToggle || !searchInput) return;

    // Update placeholder text with current section
    if (currentSection) {
      searchInput.placeholder = `Search ${currentSection.name}...`;
    }

    // Toggle search box
    searchToggle.addEventListener('click', (e) => {
      e.preventDefault();
      toggleSearchBox(searchToggle, searchBoxContainer, searchInput);
    });

    // Close search box
    if (searchCloseBtn) {
      searchCloseBtn.addEventListener('click', (e) => {
        e.preventDefault();
        closeSearchBox(searchToggle, searchBoxContainer, searchModal);
      });
    }

    // Close modal
    if (searchModalClose) {
      searchModalClose.addEventListener('click', closeSearchModal);
    }
    if (searchModalBackdrop) {
      searchModalBackdrop.addEventListener('click', closeSearchModal);
    }

    // Search input
    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.trim();

      // Clear timeout
      if (searchTimeout) clearTimeout(searchTimeout);

      // Only search if query is at least 2 characters
      if (query.length < 2) {
        closeSearchModal();
        return;
      }

      // Debounce search (300ms)
      searchTimeout = setTimeout(() => {
        performSearch(query);
      }, 300);
    });

    // ESC key to close
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeSearchBox(searchToggle, searchBoxContainer, searchModal);
      }
    });
  }

  function detectCurrentSection() {
    const path = window.location.pathname;
    for (const [key, config] of Object.entries(sectionConfig)) {
      if (path.includes(key)) {
        return config;
      }
    }
    // Default to news
    return sectionConfig['/news/'];
  }

  function toggleSearchBox(toggle, container, input) {
    const isHidden = container.classList.contains('hidden');
    if (isHidden) {
      container.classList.remove('hidden');
      toggle.classList.add('hidden');
      input.focus();
    } else {
      closeSearchBox(toggle, container);
    }
  }

  function closeSearchBox(toggle, container, modal) {
    container.classList.add('hidden');
    toggle.classList.remove('hidden');
    if (modal) closeSearchModal();
  }

  function closeSearchModal() {
    const modal = document.getElementById('search-modal');
    if (modal) {
      modal.classList.add('hidden');
    }
  }

  async function performSearch(query) {
    const config = currentSection;
    if (!config) return;

    // Show loading state
    showSearchModal();
    showLoading();

    try {
      // Load or use cached index
      let data = indexCache[config.indexUrl];
      if (!data) {
        const response = await fetch(config.indexUrl);
        if (!response.ok) {
          throw new Error('Failed to load search index');
        }
        data = await response.json();
        indexCache[config.indexUrl] = data;
      }

      // Initialize Fuse.js if not already done
      if (!currentFuse || currentFuse.config.threshold !== config.threshold) {
        currentFuse = new Fuse(data, {
          keys: config.searchKeys,
          threshold: config.threshold,
          includeScore: true,
          minMatchCharLength: 2,
          shouldSort: true
        });
      }

      // Perform search
      const results = currentFuse.search(query);

      // Render results
      renderResults(results, config, query);
    } catch (error) {
      console.error('Search error:', error);
      showError('Search unavailable. Please try again.');
    }
  }

  function renderResults(results, config, query) {
    const container = document.getElementById('search-results-container');
    const noResults = document.getElementById('search-no-results');
    const loading = document.getElementById('search-loading');

    if (!container) return;

    // Hide loading
    if (loading) loading.classList.add('hidden');

    if (results.length === 0) {
      container.innerHTML = '';
      if (noResults) {
        document.getElementById('search-query-text').textContent = query;
        noResults.classList.remove('hidden');
      }
      return;
    }

    if (noResults) noResults.classList.add('hidden');

    // Render results
    container.innerHTML = results
      .slice(0, 20) // Limit to 20 results
      .map(result => config.formatResult(result.item))
      .join('');

    // Add click handlers to results
    container.querySelectorAll('.search-result-item').forEach(item => {
      item.addEventListener('click', (e) => {
        const url = item.dataset.url;
        if (url) {
          window.location.href = url;
        }
      });
    });
  }

  function showSearchModal() {
    const modal = document.getElementById('search-modal');
    if (modal) {
      modal.classList.remove('hidden');
    }
  }

  function showLoading() {
    const container = document.getElementById('search-results-container');
    const loading = document.getElementById('search-loading');
    const noResults = document.getElementById('search-no-results');

    if (container) container.innerHTML = '';
    if (noResults) noResults.classList.add('hidden');
    if (loading) loading.classList.remove('hidden');
  }

  function showError(message) {
    const container = document.getElementById('search-results-container');
    if (container) {
      container.innerHTML = `<div style="padding: 2rem; text-align: center; color: #dc2626;">${message}</div>`;
    }
  }

  // Format functions for different result types
  function formatNewsResult(item) {
    const tagsHtml = item.tags ? item.tags.map(tag =>
      `<span class="search-result-tag">${escapeHtml(tag)}</span>`
    ).join('') : '';

    return `
      <div class="search-result-item" data-url="${escapeHtml(item.url)}">
        <div class="search-result-title">${escapeHtml(item.title)}</div>
        <div class="search-result-meta">
          ${item.date ? `<span>${escapeHtml(item.date)}</span>` : ''}
          ${item.category ? `<span> • ${escapeHtml(item.category)}</span>` : ''}
          ${item.company ? `<span> • ${escapeHtml(item.company)}</span>` : ''}
        </div>
        <div class="search-result-excerpt">${escapeHtml(item.summary)}</div>
      </div>
    `;
  }

  function formatCompanyResult(item) {
    return `
      <div class="search-result-item" data-url="${escapeHtml(item.url)}">
        <div class="search-result-title">${escapeHtml(item.title)}</div>
        <div class="search-result-meta">
          ${item.headquarters ? `<span>📍 ${escapeHtml(item.headquarters)}</span>` : ''}
          ${item.company_type ? `<span> • ${escapeHtml(item.company_type)}</span>` : ''}
        </div>
        <div class="search-result-excerpt">${escapeHtml(item.description)}</div>
      </div>
    `;
  }

  function formatGlossaryResult(item) {
    return `
      <div class="search-result-item" data-url="${escapeHtml(item.url)}">
        <div class="search-result-title">${escapeHtml(item.title)}</div>
        ${item.aka ? `<div class="search-result-meta">aka: ${escapeHtml(item.aka)}</div>` : ''}
        <div class="search-result-excerpt">${escapeHtml(item.summary)}</div>
      </div>
    `;
  }

  function formatBlogResult(item) {
    const tagsHtml = item.tags ? item.tags.map(tag =>
      `<span class="search-result-tag">${escapeHtml(tag)}</span>`
    ).join('') : '';

    return `
      <div class="search-result-item" data-url="${escapeHtml(item.url)}">
        <div class="search-result-title">${escapeHtml(item.title)}</div>
        <div class="search-result-meta">
          ${item.date ? `<span>${escapeHtml(item.date)}</span>` : ''}
          ${item.author ? `<span> • By ${escapeHtml(item.author)}</span>` : ''}
        </div>
        <div class="search-result-excerpt">${escapeHtml(item.summary)}</div>
      </div>
    `;
  }

  function formatEventResult(item) {
    return `
      <div class="search-result-item" data-url="${escapeHtml(item.url)}">
        <div class="search-result-title">${escapeHtml(item.title)}</div>
        <div class="search-result-meta">
          ${item.event_date ? `<span>${escapeHtml(item.event_date)}</span>` : ''}
          ${item.location ? `<span> • 📍 ${escapeHtml(item.location)}</span>` : ''}
          ${item.event_type ? `<span> • ${escapeHtml(item.event_type)}</span>` : ''}
        </div>
        <div class="search-result-excerpt">${escapeHtml(item.description)}</div>
      </div>
    `;
  }

  // Utility function to escape HTML
  function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }
})();
