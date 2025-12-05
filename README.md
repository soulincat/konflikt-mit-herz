# Konflikt-Kompetenz mit Herz - Landing Page

Bilingual (German/English) landing page for Soulful Academy's conflict resolution training program.

## Features

- 🌍 Bilingual support (German/English) with language toggle
- 📱 Responsive layout
- 🎨 Clean, content-focused structure
- 💾 Language preference saved in browser

## Development Setup

### Prerequisites

- Node.js (v14 or higher) - [Download here](https://nodejs.org/)
- npm (comes with Node.js)

### Installation

1. Install dependencies (optional - uses npx for dev server):
```bash
npm install
```

### Running the Development Server

Start a local development server:

```bash
npm run dev
```

Or:

```bash
npm start
```

The page will be available at: `http://localhost:3000`

### Opening in Browser

To automatically open in your default browser:

```bash
npm run open
```

## Project Structure

```
konflikt_mit_herz/
├── index.html          # Main landing page (all content)
├── package.json        # Project configuration
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## Development Notes

- All styles and scripts are currently inline in `index.html`
- Language toggle persists preference using localStorage
- The page is fully functional as a single HTML file

## Future Enhancements

Consider separating into:
- `css/styles.css` - Styles
- `js/main.js` - JavaScript functionality
- `assets/` - Images and other media

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile responsive

## License

ISC

