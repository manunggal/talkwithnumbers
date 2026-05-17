# Talk With Numbers

A data-driven web platform for discussing decarbonization through quantitative analysis — not just opinion.

🔗 **[Live Site → talkwithnumbers.com](https://www.talkwithnumbers.com)**

> *"This heated debate is fundamentally about numbers... actual numbers are rarely mentioned."*
> — David J MacKay, Sustainability without Hot Air

---

## Motivation

Energy and climate debates are too often driven by adjectives rather than data. This site is built on the premise that informed decisions on decarbonization require actual numbers — magnitudes, costs, trade-offs — presented clearly enough to support honest evaluation.

Inspired by David MacKay's *Sustainability without Hot Air*, the platform aims to bring quantitative rigour to topics in energy transition, covering hydrogen production, wind energy, and maritime decarbonization.

## What's inside

| Section | URL | Status | Description |
|---|---|---|---|
| Hydrogen | `/hydrogen/h2-production/` | ✅ Live | Interactive dashboard for green hydrogen production scenarios — CO₂ emissions and electricity requirements as a function of electrolyzer efficiency and renewable energy share |
| Wind Energy | `/windenergy/` | 🚧 In progress | Planned coverage of wind energy numbers; currently links to the RAM simulation tool |
| Maritime Decarbonization | `/mardecarb/` | ✅ Live | Quantitative analysis of battery-electric propulsion feasibility for Indonesian cargo shipping routes, based on Kistner et al. (2023) |

## Hydrogen dashboard

The H2 production dashboard at `/hydrogen/h2-production/` lets users explore how key variables affect the environmental footprint and infrastructure requirements of green hydrogen:

- Total electricity requirement (TWh)
- Total hydrogen production (megatonnes/year)
- Number of required 20 MW electrolyzers
- Total CO₂e emissions (megatonnes)

Input parameters include electrolyzer efficiency, grid renewable energy share, and CO₂e emission factor for fossil fuel generation. Charts update interactively as parameters change.

## Maritime decarbonization article

The mardecarb section contains a data-driven analysis of electrifying Indonesian cargo ship propulsion, using the T-10 Sea-Toll route (Surabaya → North Maluku) as a case study. The analysis applies economic and physical models from peer-reviewed literature to compare battery-electric vs. diesel propulsion across route segments of varying length.

Key finding: battery-electric propulsion is economically viable for short passages (under ~24 hours), but investment costs remain 50× higher than diesel for long routes such as Surabaya–Tidore (~3 days).

## Tech stack

- **Django** — web framework and URL routing
- **Python** — backend logic and data processing
- **JavaScript / Chart.js** — interactive frontend charts
- **HTML / CSS / SCSS** — templating and styling (based on HTML5 UP Stellar theme)
- **SQLite** — lightweight database
- **Heroku** — deployment platform (via Procfile)

## Project structure

```
talkwithnumbers/
├── hydrogen/          # Hydrogen production dashboard app
├── windenergy/        # Wind energy section (in progress)
├── mardecarb/         # Maritime decarbonization articles
├── talkwithnumbers/   # Django project settings
├── templates/         # Shared HTML templates
├── static/            # Static assets (images, CSS, JS)
├── manage.py
├── requirements.txt
└── Procfile           # Heroku deployment config
```

## Run locally

```bash
# Clone the repo
git clone https://github.com/manunggal/talkwithnumbers.git
cd talkwithnumbers

# Install dependencies
pip install -r requirements.txt

# Run the development server
python manage.py runserver
```

Then open `http://127.0.0.1:8000` in your browser.

## Status and roadmap

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Platform](https://img.shields.io/badge/platform-Django-092E20)
![Deployed](https://img.shields.io/badge/deployed-Heroku-430098)

The site is live and actively maintained. Planned additions:

- [ ] Wind energy section — numbers on offshore wind capacity, capacity factors, and LCOE
- [ ] Extended maritime decarbonization coverage — ammonia, methanol, LNG as transition fuels
- [ ] Integration with the [`Offshore-Wind-Farm-RAM-Simulation`](https://github.com/manunggal/Offshore-Wind-Farm-RAM-Simulation) tool

## Author

**Manunggal Sukendro** — Reliability engineer with a focus on offshore energy systems and decarbonization.  
[github.com/manunggal](https://github.com/manunggal) · [linkedin.com/in/manunggal-sukendro-3077b91a](https://www.linkedin.com/in/manunggal-sukendro-3077b91a/)
