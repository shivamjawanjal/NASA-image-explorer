    // NASA Image Search Application
    class NASASearch {
        constructor() {
            this.searchForm = document.getElementById('searchForm');
            this.searchInput = document.getElementById('searchQuery');
            this.loadingDiv = document.getElementById('loading');
            this.resultsDiv = document.getElementById('results');
            
            this.init();
        }
        
        init() {
            // Add event listener to search form
            this.searchForm.addEventListener('submit', (e) => {
                e.preventDefault();
                this.performSearch();
            });
            
            // Check for saved search in URL
            const urlParams = new URLSearchParams(window.location.search);
            const query = urlParams.get('q');
            if (query) {
                this.searchInput.value = query;
                this.performSearch();
            }
        }
        
        async performSearch() {
            const query = this.searchInput.value.trim();
            if (!query) return;
            
            // Show loading
            this.showLoading(true);
            
            // Update URL
            const url = new URL(window.location);
            url.searchParams.set('q', query);
            window.history.pushState({}, '', url);
            
            try {
                const response = await fetch(`/api/search?q=${encodeURIComponent(query)}&media_type=image`);
                const data = await response.json();
                
                if (data.success) {
                    this.displayResults(data);
                } else {
                    this.displayError(data.error || 'An error occurred');
                }
            } catch (error) {
                console.error('Search failed:', error);
                this.displayError('Failed to connect to the server');
            } finally {
                this.showLoading(false);
            }
        }
        
        displayResults(data) {
            if (!data.results || data.results.length === 0) {
                this.resultsDiv.innerHTML = `
                    <div class="no-results">
                        <div class="no-results-icon">🔭</div>
                        <h3>No results found for "${data.query}"</h3>
                        <p>Try different keywords or check your spelling</p>
                    </div>
                `;
                return;
            }
            
            let html = `
                <div class="results-count">
                    Found ${data.total} results for "${data.query}"
                </div>
                <div class="results-grid">
            `;
            
            data.results.forEach(item => {
                const previewImage = item.images && item.images.length > 0 
                    ? item.images.find(img => img.rel === 'preview') || item.images[0]
                    : null;
                
                const imageUrl = previewImage ? previewImage.href : '';
                const date = item.date_created ? new Date(item.date_created).toLocaleDateString() : 'Unknown date';
                
                html += `
                    <div class="result-card">
                        ${imageUrl ? 
                            `<img src="${imageUrl}" alt="${item.title}" class="result-image" 
                                onerror="this.src='https://images-assets.nasa.gov/image/PIA12235/PIA12235~thumb.jpg'">` : 
                            `<div class="result-image" style="display: flex; align-items: center; justify-content: center; background: #e9ecef;">
                                <span style="color: #999;">No preview</span>
                            </div>`
                        }
                        
                        <div class="result-content">
                            <div class="result-title">${this.escapeHtml(item.title)}</div>
                            <div class="result-description">${this.escapeHtml(item.description.substring(0, 200))}${item.description.length > 200 ? '...' : ''}</div>
                            
                            <div class="result-meta">
                                ${item.center ? `<span class="result-center">${item.center}</span>` : ''}
                                <span class="result-date">${date}</span>
                            </div>
                            
                            ${item.keywords && item.keywords.length > 0 ? `
                                <div class="result-keywords">
                                    ${item.keywords.slice(0, 5).map(keyword => 
                                        `<span class="keyword-tag">${this.escapeHtml(keyword)}</span>`
                                    ).join('')}
                                </div>
                            ` : ''}
                            
                            <div class="result-links">
                                ${item.images && item.images.length > 0 ? 
                                    item.images.slice(0, 2).map(img => 
                                        `<a href="${img.href}" target="_blank" class="result-link">${img.rel || 'Image'}</a>`
                                    ).join('') : ''
                                }
                                <a href="https://images.nasa.gov/details-${item.id}" target="_blank" class="result-link">Details</a>
                            </div>
                        </div>
                    </div>
                `;
            });
            
            html += '</div>';
            this.resultsDiv.innerHTML = html;
        }
        
        displayError(message) {
            this.resultsDiv.innerHTML = `
                <div class="error-message">
                    ${this.escapeHtml(message)}
                </div>
            `;
        }
        
        showLoading(show) {
            this.loadingDiv.style.display = show ? 'block' : 'none';
            this.resultsDiv.style.opacity = show ? '0.5' : '1';
        }
        
        escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
    }

    // Initialize the application when the page loads
    document.addEventListener('DOMContentLoaded', () => {
        new NASASearch();
    });