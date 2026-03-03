NASA Image and Video Library Search 🚀
https://images-assets.nasa.gov/image/PIA12235/PIA12235~thumb.jpg

A full-stack web application that provides a beautiful, intuitive interface for searching and exploring NASA's vast collection of space imagery and videos. Built with Python/Flask and vanilla JavaScript, this app makes the cosmos accessible to everyone!

📸 Screenshots
[Add screenshots of your application here]

✨ Features
🔍 Smart Search - Search NASA's entire media library with keywords

🖼️ Image Previews - Instant thumbnail previews for search results

📱 Responsive Design - Works seamlessly on desktop, tablet, and mobile

🏷️ Rich Metadata - View titles, descriptions, dates, and keywords

🔗 Direct Links - Access original images and official NASA pages

⚡ Real-time Results - Fast, asynchronous search experience

📋 Shareable URLs - Search queries saved in URL for easy sharing

🎨 Modern UI - Clean, gradient-based design with smooth animations

🛠️ Tech Stack
Backend
Python 3.9+ - Core programming language

Flask - Lightweight web framework

Requests - HTTP client for API calls

Flask-CORS - Cross-origin resource sharing

Frontend
HTML5 - Semantic markup

CSS3 - Modern styling with Flexbox/Grid

JavaScript (ES6) - Dynamic interactions and API calls

NASA API - Official NASA Image and Video Library API

Deployment
Vercel - Serverless deployment platform

Gunicorn - WSGI HTTP server

📦 Installation
Prerequisites
Python 3.9 or higher

pip (Python package manager)

Git (optional)

Local Setup
Clone the repository

bash
git clone https://github.com/yourusername/nasa-image-search.git
cd nasa-image-search
Create a virtual environment (recommended)

bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Run the application locally

bash
python app.py
Open your browser

text
http://localhost:5000
🚀 Deployment on Vercel
Deploy with One Click
https://vercel.com/button

Manual Deployment
Install Vercel CLI

bash
npm install -g vercel
Login to Vercel

bash
vercel login
Deploy

bash
vercel
For production deployment

bash
vercel --prod
📁 Project Structure
text
nasa-image-search/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel configuration
├── .vercelignore         # Files to ignore in deployment
├── runtime.txt           # Python version specification
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # Stylesheet
│   └── js/
│       └── app.js        # Frontend JavaScript
└── README.md             # Project documentation
🔌 API Endpoints
Search Images
text
GET /api/search?q={query}&media_type=image
Response:

json
{
  "success": true,
  "query": "moon",
  "total": 100,
  "results": [
    {
      "id": "PIA12235",
      "title": "Nearside of the Moon",
      "description": "Nearside of the Moon",
      "date_created": "2009-09-24T18:00:22Z",
      "center": "JPL",
      "keywords": ["Moon", "Chandrayaan-1"],
      "images": [...]
    }
  ]
}
Get Asset Manifest
text
GET /api/asset/{nasa_id}
Get Metadata Location
text
GET /api/metadata/{nasa_id}
🎯 Usage Examples
Search for Moon Images
text
https://your-app.vercel.app/?q=moon
Search for Mars Rover Photos
text
https://your-app.vercel.app/?q=mars%20rover
Search for Earth from Space
text
https://your-app.vercel.app/?q=earth%20from%20space
🤝 Contributing
Contributions are welcome! Here's how you can help:

Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
NASA Image and Video Library for providing the amazing API

NASA API Documentation for comprehensive guides

All the space enthusiasts who inspired this project

📧 Contact
Your Name - @yourtwitter - email@example.com

Project Link: https://github.com/yourusername/nasa-image-search
Live Demo: https://your-app.vercel.app

🚀 Future Enhancements
Add video search support

Implement pagination for more results

Add filtering by center/year

Create dark/light theme toggle

Add favorites/bookmark feature

Implement image download option

Add related images suggestions

Create space news integration

⭐ Show Your Support
If you found this project helpful, please give it a ⭐ on GitHub!
