#!/usr/bin/env python3
"""
NASA Image and Video Library Search Application
Backend API server - Production ready for Vercel
"""

import requests
from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS
import os

# Initialize Flask app
app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)  # Enable CORS for frontend development

# NASA API base URL
NASA_API_URL = "https://images-api.nasa.gov"

# Get the current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    """Serve the main HTML page"""
    try:
        return send_from_directory(os.path.join(BASE_DIR, 'templates'), 'index.html')
    except Exception as e:
        return f"Error loading template: {str(e)}", 500

@app.route('/static/<path:path>')
def serve_static(path):
    """Serve static files"""
    return send_from_directory(os.path.join(BASE_DIR, 'static'), path)

@app.route('/api/search')
def search():
    """Search NASA images and return JSON data"""
    query = request.args.get('q', '')
    media_type = request.args.get('media_type', 'image')
    
    if not query:
        return jsonify({'error': 'No search query provided'}), 400
    
    try:
        # Make request to NASA API
        params = {
            'q': query,
            'media_type': media_type
        }
        
        print(f"Searching NASA API for: {query}")
        
        response = requests.get(
            f"{NASA_API_URL}/search",
            params=params,
            timeout=10
        )
        
        response.raise_for_status()
        data = response.json()
        
        # Format the response for easier frontend consumption
        formatted_results = format_search_results(data)
        
        return jsonify({
            'success': True,
            'query': query,
            'results': formatted_results,
            'total': len(formatted_results)
        })
        
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/asset/<nasa_id>')
def get_asset(nasa_id):
    """Get asset manifest for a specific NASA ID"""
    try:
        response = requests.get(f"{NASA_API_URL}/asset/{nasa_id}", timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/metadata/<nasa_id>')
def get_metadata(nasa_id):
    """Get metadata location for a specific NASA ID"""
    try:
        response = requests.get(f"{NASA_API_URL}/metadata/{nasa_id}", timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

def format_search_results(data):
    """Format NASA API response for easier frontend consumption"""
    formatted = []
    
    if not data or 'collection' not in data or 'items' not in data['collection']:
        return formatted
    
    for item in data['collection']['items']:
        try:
            formatted_item = {
                'id': item['data'][0]['nasa_id'] if item.get('data') else None,
                'title': item['data'][0]['title'] if item.get('data') else 'Untitled',
                'description': item['data'][0].get('description', 'No description available'),
                'date_created': item['data'][0].get('date_created', ''),
                'center': item['data'][0].get('center', ''),
                'keywords': item['data'][0].get('keywords', []),
                'media_type': item['data'][0].get('media_type', 'image'),
                'images': []
            }
            
            # Get all image links
            if item.get('links'):
                for link in item['links']:
                    if link.get('href') and link.get('render') == 'image':
                        formatted_item['images'].append({
                            'href': link['href'],
                            'rel': link.get('rel', ''),
                            'width': link.get('width', 0),
                            'height': link.get('height', 0),
                            'size': link.get('size', 0)
                        })
            
            formatted.append(formatted_item)
        except Exception as e:
            print(f"Error formatting item: {e}")
            continue
    
    return formatted

# This is for local development
if __name__ == '__main__':
    print("🚀 NASA Image and Video Library API Server")
    print("=" * 50)
    print("Starting backend server...")
    print("API endpoint: http://localhost:5000/api/search?q=moon")
    print("Frontend: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Create templates and static directories if they don't exist
    os.makedirs(os.path.join(BASE_DIR, 'templates'), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, 'static', 'css'), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, 'static', 'js'), exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)

# This is for Vercel
# Vercel needs a variable named 'app' to be the WSGI application
# The Flask app instance is already named 'app', so we're good