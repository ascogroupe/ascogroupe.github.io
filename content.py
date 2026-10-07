"""Content data for the ASCO Groupe site. Consumed by build.py."""

def IMG(cat, name):
    return f"assets/img/{cat}/{name}"

SITE = {
    "name": "ASCO Groupe",
    "phone_display": "+229 95 95 99 99",
    "phone_tel": "+22995959999",
    "phone_togo_display": "+228 90 22 99 99",
    "phone_togo_tel": "+22890229999",
    "fax_display": "+229 21 37 74 70",
    "email": "info@asco-groupe.com",
    "whatsapp": "22890229999",
    "address_line1": "Ilot 6220, Parcelle N, 3è rue après carrefour Abattoir (Route de Porto-Novo)",
    "address_line2": "05 BP 630 Cotonou, République du Bénin",
    "maps_embed_src": "https://www.google.com/maps/embed?pb=!1m3!3m2!1m1!4s16656664199868773893",
    "maps_link": "https://www.google.com/maps/place/Soci%C3%A9t%C3%A9+ASCO+SARL/@6.3624533,2.3971371,17z/data=!3m1!4b1!4m6!3m5!1s0x103cab3cbdbfb90d:0xe7285bd6c824f605!8m2!3d6.3624533!4d2.3971371!16s%2Fg%2F11g0clxgxx",
}

NAV = {
    "menuiserie": [
        ("Ouvrages sur paumelles", "ouvrages-sur-paumelles.html"),
        ("Ouvrages coulissants", "ouvrages-coulissants.html"),
        ("Stores", "stores.html"),
        ("Façades", "facades.html"),
        ("Rampes", "rampes.html"),
        ("Vitrages", "vitrages.html"),
    ],
    "automatisation": [
        ("Portails coulissants", "portails-coulissants.html"),
        ("Portails à battants", "portails-a-battants.html"),
        ("Portails de garages sectionnelles", "portails-garages-sectionnelles.html"),
        ("Portes coulissantes automatiques", "portes-coulissantes-automatiques.html"),
        ("Portes sur paumelles automatiques", "portes-sur-paumelles-automatiques.html"),
        ("Barrières & réservation de parking", "barriere-reservation-parking.html"),
        ("Rideaux métalliques & vasistas", "rideaux-metalliques-vasistas.html"),
        ("Bornes escamotables", "bornes-escamotables.html"),
        ("Accessoires", "accessoires.html"),
    ],
    "acces": [
        ("Hôtelier", "solutions-dacces.html#hotelier"),
        ("Industriel", "solutions-dacces.html#industriel"),
        ("Clés sur organigramme", "solutions-dacces.html#organigramme"),
        ("Véhicules", "solutions-dacces.html#vehicules"),
    ],
}

CLIENT_LOGOS = [
    {"file": "novotel.png", "name": "Novotel"},
    {"file": "ibis.png", "name": "Ibis"},
    {"file": "azalai.png", "name": "Azalai Hotels"},
    {"file": "ivotel.png", "name": "Ivotel"},
    {"file": "mercure.png", "name": "Mercure"},
    {"file": "sheraton.png", "name": "Sheraton"},
    {"file": "ecobank.png", "name": "Ecobank"},
    {"file": "pullman.png", "name": "Pullman"},
    {"file": "palmbeach.png", "name": "Palm Beach Hotels"},
]

CLIENTS_MORE = (
    "+ de nombreux clients privés et institutionnels au Bénin, au Togo, au Sénégal, "
    "au Mali, au Burkina Faso, en Côte d'Ivoire, au Ghana et en Algérie."
)

REFERENCES_BY_COUNTRY = [
    {"country": "Bénin", "clients": ["Novotel", "Ibis", "Hôtel du Port", "Vinckinfel Hôtel", "PRIMO SA", "Ecobank", "Trinity Forex", "Groupe Betsaleel Building"]},
    {"country": "Togo", "clients": ["Mercure Sarakawa", "Ibis Lomé", "Palm Beach Lomé", "Hôtel Clémentine", "Africom"]},
    {"country": "Côte d'Ivoire", "clients": ["Pullman Abidjan", "Novotel Abidjan", "Ibis Marcory", "Ibis Plateau", "Ivotel"]},
    {"country": "Mali", "clients": ["Azalai Grand Hôtel", "Hôtel Salam", "Hôtel Nord Sud"]},
    {"country": "Sénégal · Burkina Faso", "clients": ["Palm Beach Sénégal", "Hôtel Independence", "Ecobank Burkina Faso"]},
    {"country": "Ghana · Algérie", "clients": ["Novotel Accra", "Sheraton Accra", "Ibis Alger"]},
]

# ---------------------------------------------------------------------------
# PAGES
# ---------------------------------------------------------------------------
PAGES = []

def add(page):
    PAGES.append(page)

# ============================================================ HOME =========
add({
    "slug": "index.html",
    "template": "home",
    "title": "Menuiserie Aluminium, Solutions d'Accès & Ouvertures Automatisées",
    "description": "ASCO Groupe, société africaine spécialiste de la menuiserie aluminium, des solutions d'accès et des ouvertures automatisées. Présente dans toute l'Afrique, avec un réseau de partenaires internationaux.",
    "nav_active": "home",
    "hero": {
        "slides": [
            IMG("hero", "men-alum3.jpg"),
            IMG("hero", "ouvert-auto-1.jpg"),
            IMG("hero", "paddedimage723390-serrure.jpg"),
            IMG("hero", "men-alum1.jpg"),
            IMG("hero", "ouvert-auto-4.jpg"),
        ],
        "title": "Plus de <span>design</span>, plus de sécurité, et de bien-être.",
        "lead": "ASCO Groupe est une société africaine spécialisée dans la menuiserie aluminium, les solutions d'accès et les systèmes d'ouverture automatisée. Nous équipons entreprises, banques, hôtels et résidences à travers l'Afrique et au-delà, appuyés par un réseau de partenaires internationaux.",
        "cta": {"label": "Découvrir nos produits", "href": "menuiserie-aluminium.html"},
        "cta2": {"label": "Qui sommes-nous", "href": "a-propos.html"},
        "stats": [
            {"num": "3", "label": "Métiers complémentaires"},
            {"num": "Afrique", "label": "Présence régionale, réseau international"},
            {"num": "20+", "label": "Grandes références clients"},
            {"num": "100%", "label": "Installation & SAV locaux"},
        ],
    },
    "pillars": [
        {"icon": "window", "title": "Menuiserie Aluminium", "text": "Fenêtres, baies, façades et vitrages sur-mesure, alliant finesse des lignes et solidité certifiée.", "href": "menuiserie-aluminium.html"},
        {"icon": "gate", "title": "Ouvertures Automatisées", "text": "Portails coulissants, à battants, portes automatiques et bornes escamotables pour tous les usages.", "href": "ouvertures-automatisees.html"},
        {"icon": "key", "title": "Solutions d'Accès", "text": "Serrures électroniques, cylindres sur organigramme et contrôle d'accès pour sécuriser tous vos sites.", "href": "solutions-dacces.html"},
    ],
    "sections": [
        {
            "type": "split", "id": "efficacite",
            "eyebrow": "Efficacité redoutable",
            "title": "ASCO, le partenaire <span>idéal</span> pour vos projets",
            "lead": "ASCO est une société africaine spécialisée dans la menuiserie aluminium, les contrôles d'accès et les systèmes d'ouverture automatisée.",
            "paragraphs": [
                "Notre ambition est de vous offrir, sur l'ensemble de nos produits et prestations, des ouvrages de fermeture alliant esthétique, sécurité et confort d'ouverture, d'où l'alliance de nos spécialités et la complémentarité de nos gammes de produits.",
                "Grâce à la mise à jour permanente de nos techniciens et à nos partenariats avec de grandes marques européennes, ASCO s'est imposée comme une société de référence, compétitive à l'échelle nationale et sous-régionale, dans toute l'Afrique.",
            ],
            "bullets": [
                "Techniciens formés en continu, partenaires européens de référence",
                "Présence commerciale et service après-vente dans toute l'Afrique, appuyée par un réseau international",
                "Clients de renom : Novotel, Ibis, Ecobank, Sheraton…",
            ],
            "cta": {"label": "Qui sommes-nous", "href": "a-propos.html"},
            "image": IMG("hero", "men-alum1.jpg"),
            "badge": {"icon": "award", "text": "Référence régionale"},
        },
        {
            "type": "category-grid", "bg": "alt", "id": "metiers",
            "eyebrow": "Nos métiers", "cols": 3,
            "title": "Trois expertises, <span>une seule</span> exigence",
            "lead": "Découvrez nos trois familles de produits, conçues pour l'habitat, le tertiaire et l'industrie.",
            "cards": [
                {"image": IMG("hero", "men-alum3.jpg"), "tag": "Menuiserie", "title": "Menuiserie Aluminium", "text": "Fenêtres, portes, vérandas et façades vitrées sur-mesure.", "href": "menuiserie-aluminium.html"},
                {"image": IMG("hero", "ouvert-auto-1.jpg"), "tag": "Automatisation", "title": "Ouvertures Automatisées", "text": "Portails, portes et barrières motorisés pour tous les usages.", "href": "ouvertures-automatisees.html"},
                {"image": IMG("solutions-acces", "sol-access-3-.jpg"), "tag": "Sécurité", "title": "Solutions d'Accès", "text": "Serrures, cylindres et contrôle d'accès résidentiel, tertiaire & industriel.", "href": "solutions-dacces.html"},
            ],
        },
        {
            "type": "timeline", "id": "services-home",
            "eyebrow": "Nos services",
            "title": "Un accompagnement <span>de bout en bout</span>",
            "lead": "De l'étude à la maintenance, ASCO reste à vos côtés à chaque étape de votre projet.",
            "cards": [
                {"title": "Organisation-conseil", "text": "Nous vous accompagnons dans la définition d'une solution adaptée à vos besoins, dans le choix et la combinaison des fournitures."},
                {"title": "Installation & mise en service", "text": "Nos techniciens assurent l'installation complète du système au sein de votre entreprise, avec un suivi régulier de l'avancement."},
                {"title": "Formation", "text": "Notre centre de formation prépare vos équipes aux aspects techniques et fonctionnels des solutions déployées."},
                {"title": "Hotline, entretien & dépannage", "text": "Une hotline technique et des contrats de maintenance pour une intervention rapide, assurée par des techniciens expérimentés."},
            ],
        },
        {
            "type": "clients", "bg": "alt", "id": "clients-home",
            "eyebrow": "Ils nous font confiance",
            "title": "Des références dans toute <span>l'Afrique</span>",
            "lead": "Entreprises, banques, hôtels et grands groupes nous confient la sécurité et le confort de leurs sites depuis de nombreuses années.",
            "logos": CLIENT_LOGOS,
            "more": CLIENTS_MORE,
        },
        {
            "type": "cta-banner",
            "title": "Un projet à sécuriser ou à moderniser ?",
            "text": "Nos équipes étudient votre demande et vous recontactent rapidement.",
            "primary": {"label": "Demander un devis", "href": "contact.html"},
            "secondary": {"label": "Appeler maintenant", "href": "tel:+22995959999"},
        },
    ],
})

# ========================================================= A PROPOS ========
add({
    "slug": "a-propos.html",
    "template": "inner",
    "title": "Qui sommes-nous",
    "description": "ASCO est une société africaine spécialisée dans la menuiserie aluminium, les contrôles d'accès et les systèmes d'ouverture automatisée.",
    "hero": {
        "image": IMG("hero", "men-alum2.jpg"),
        "eyebrow": "Efficacité redoutable",
        "title": "Qui sommes-nous ?",
        "lead": "Une société africaine, trois expertises complémentaires, un même souci du détail sur chaque projet.",
        "breadcrumb": [("Accueil", "index.html"), ("À propos", "a-propos.html")],
    },
    "sections": [
        {
            "type": "split",
            "eyebrow": "Notre histoire",
            "title": "Une ambition : des ouvrages qui allient <span>esthétique et sécurité</span>",
            "paragraphs": [
                "ASCO est une société africaine spécialisée dans la menuiserie aluminium, les contrôles d'accès et les systèmes d'ouverture automatisée.",
                "Notre ambition est de vous offrir, sur l'ensemble de nos produits et prestations, des ouvrages de fermeture alliant esthétique, sécurité et confort d'ouverture, d'où l'alliance de nos spécialités et la complémentarité de nos gammes de produits.",
                "Grâce à la mise à jour permanente des compétences de nos techniciens et à nos partenariats avec de grandes marques européennes, ASCO est une société compétitive sur le plan national et sous-régional, centrée sur la satisfaction client et le maintien d'une image forte, une référence qui continue de faire ses preuves dans toute l'Afrique.",
            ],
            "bullets": [
                "Trois métiers intégrés : menuiserie aluminium, solutions d'accès, ouvertures automatisées",
                "Partenariats avec de grandes marques européennes",
                "Equipes techniques formées en continu",
            ],
            "image": IMG("divers", "reference.jpg"),
        },
        {
            "type": "split", "reverse": True, "bg": "alt",
            "eyebrow": "Notre promesse",
            "title": "La société ASCO, <span>votre partenaire</span>",
            "paragraphs": [
                "De nombreux clients du Bénin et de la sous-région nous font déjà confiance. La société ASCO est votre partenaire : nous proposons des solutions innovantes ainsi que les meilleures prestations de services pour la protection des personnes et des biens.",
                "Nous sommes passionnés et présents pour nos clients. Notre objectif : dépasser leurs attentes.",
            ],
            "image": IMG("hero", "ouvert-auto-2.jpg"),
            "cta": {"label": "Découvrir nos services", "href": "services.html"},
        },
        {
            "type": "stats-navy",
            "eyebrow": "En chiffres",
            "title": "Une empreinte <span>panafricaine</span>",
            "stats": [
                {"num": "3", "label": "Métiers complémentaires"},
                {"num": "Afrique", "label": "Présence régionale, réseau international"},
                {"num": "20+", "label": "Grandes références clients"},
                {"num": "100%", "label": "SAV & techniciens locaux"},
            ],
        },
        {
            "type": "cta-banner",
            "title": "Envie de rejoindre nos références ?",
            "text": "Parlons de votre projet de menuiserie, d'automatisation ou de contrôle d'accès.",
            "primary": {"label": "Nous contacter", "href": "contact.html"},
        },
    ],
})

# ========================================================== SERVICES =======
add({
    "slug": "services.html",
    "template": "inner",
    "title": "Services & Références",
    "description": "Hotline, organisation-conseil, installation, formation et maintenance : découvrez les services ASCO et les grands groupes qui nous font confiance en Afrique.",
    "hero": {
        "image": IMG("divers", "organi-conseils.jpg"),
        "eyebrow": "Nous sommes les meilleurs",
        "title": "Nos services",
        "lead": "Un accompagnement complet : conseil, installation, formation, maintenance et dépannage, assurés par nos propres techniciens.",
        "breadcrumb": [("Accueil", "index.html"), ("Services", "services.html")],
    },
    "sections": [
        {
            "type": "timeline", "id": "nos-services",
            "eyebrow": "De l'étude au SAV",
            "title": "Un service complet, <span>à chaque étape</span>",
            "lead": "L'accompagnement que nous mettons à votre disposition nous conduit naturellement à proposer un suivi complet de votre projet.",
            "cards": [
                {"title": "Hotline", "text": "Une hotline technique destinée à répondre efficacement à vos questions aux heures ouvrables."},
                {"title": "Organisation-conseil", "text": "Nous vous accompagnons dans la définition d'une solution répondant à vos besoins, dans le choix et la combinaison des fournitures les plus adaptées."},
                {"title": "Installation et mise en service", "text": "Nos techniciens assurent l'installation de la totalité du système au sein de votre entreprise et en réalisent la mise en service. Vos collaborateurs sont informés tout au long du déploiement. La réception effectuée, nous vous remettons une solution prête à l'emploi."},
                {"title": "Formation", "text": "Nous disposons d'un centre de formation où nous formons des élèves ayant fait au moins la classe de 4ième sur nos spécialités, ainsi qu'une offre de formation sur les aspects techniques et fonctionnels de la solution déployée."},
                {"title": "Maintenance", "text": "La maintenance de nos installations, encadrée par une offre complète de contrats disponibles, vous rend privilégié parmi nos nombreux clients, avec une intervention et une satisfaction immédiates."},
                {"title": "Entretien et dépannage", "text": "Assurer une proximité client, gage de réactivité, est une mission à laquelle ASCO accorde une très grande importance. Une équipe de techniciens expérimentés assure un SAV performant aux heures ouvrables."},
            ],
        },
        {
            "type": "country-grid", "bg": "alt", "id": "references",
            "eyebrow": "Ils nous font confiance",
            "title": "Nos références, <span>pays par pays</span>",
            "lead": "De nombreux clients du Bénin et de la sous-région nous font déjà confiance.",
            "cards": REFERENCES_BY_COUNTRY,
        },
        {
            "type": "clients",
            "eyebrow": "Grandes enseignes",
            "title": "Ils nous ont choisis",
            "logos": CLIENT_LOGOS,
            "more": CLIENTS_MORE,
        },
        {
            "type": "cta-banner",
            "title": "Besoin d'un contrat de maintenance ?",
            "text": "Nos équipes techniques interviennent rapidement sur l'ensemble de nos installations.",
            "primary": {"label": "Demander un devis", "href": "contact.html"},
        },
    ],
})

# =================================================== MENUISERIE (cat) =======
MEN_CAT_NAV = {"title": "Menuiserie Aluminium", "overview_href": "menuiserie-aluminium.html", "cards": NAV["menuiserie"]}

add({
    "slug": "menuiserie-aluminium.html",
    "template": "inner",
    "title": "Menuiserie Aluminium",
    "description": "Fenêtres, portes, stores, façades, rampes et vitrages en aluminium sur-mesure : la menuiserie ASCO allie esthétique, solidité et normes actuelles d'isolation et de sécurité.",
    "hero": {
        "image": IMG("hero", "men-alum3.jpg"),
        "eyebrow": "Métier n°1",
        "title": "La Menuiserie <span>Aluminium</span>",
        "lead": "La finesse des lignes des ouvrages en menuiserie aluminium de ASCO allie une esthétique très élégante et une solidité remarquable.",
        "cta": {"label": "Demander un devis", "href": "contact.html"},
        "breadcrumb": [("Accueil", "index.html"), ("Menuiserie Aluminium", "menuiserie-aluminium.html")],
    },
    "sections": [
        {
            "type": "split",
            "eyebrow": "Qualité certifiée",
            "title": "Un aluminium décliné dans <span>un large choix</span> de coloris",
            "paragraphs": [
                "De qualité certifiée, l'aluminium met en valeur la décoration intérieure tout en respectant l'architecture. Les gammes de nos profilés s'adaptent à toutes les classes sociales, des habitations ordinaires jusqu'à la haute architecture.",
                "Nos services répondent aux exigences et normes actuelles en termes d'isolation thermique et phonique, et de sécurité, pour assurer une protection efficace des personnes et des biens.",
                "Des simples verres à vitre aux doubles vitrages acoustiques ou sécurisés, sans oublier les panneaux de revêtement de façade, la qualité et le design de nos produits assurent une finition irréprochable qui leur permet de s'intégrer totalement sur n'importe quelle architecture.",
            ],
            "bullets": [
                "Châssis, fenêtres, portes-fenêtres, jalousies, cloisons",
                "Ouvrages coulissants ou sur paumelles, fabriqués sur mesure",
                "Façades en murs rideaux vitrés, fibre de ciment ou panneaux Alucobond",
            ],
            "image": IMG("hero", "men-alum1.jpg"),
            "badge": {"icon": "window", "text": "Fabrication sur-mesure"},
        },
        {
            "type": "category-grid", "bg": "alt", "cols": 3,
            "eyebrow": "Notre gamme",
            "title": "Explorez nos <span>familles de produits</span>",
            "cards": [
                {"image": IMG("menuiserie", "ouvr-paumelle.jpg"), "title": "Ouvrages sur paumelles", "text": "Portes et fenêtres à la française.", "href": "ouvrages-sur-paumelles.html"},
                {"image": IMG("menuiserie", "ouvr-coulis.jpg"), "title": "Ouvrages coulissants", "text": "Portes et baies gain de place.", "href": "ouvrages-coulissants.html"},
                {"image": IMG("menuiserie", "store1.jpg"), "title": "Stores", "text": "Vénitiens et bandes verticales.", "href": "stores.html"},
                {"image": IMG("menuiserie", "facade.jpg"), "title": "Façades", "text": "Murs rideaux et revêtements.", "href": "facades.html"},
                {"image": IMG("menuiserie", "rampes.jpg"), "title": "Rampes", "text": "Garde-corps et rampes d'escalier.", "href": "rampes.html"},
                {"image": IMG("menuiserie", "vitrage.jpg"), "title": "Vitrages", "text": "Simple, acoustique, blindé.", "href": "vitrages.html"},
            ],
        },
        {
            "type": "gallery",
            "eyebrow": "Accessoires", "id": "accessoires-menuiserie",
            "title": "Les <span>accessoires</span> de finition",
            "lead": "Poignées, charnières et quincaillerie assortis à chaque gamme pour une finition irréprochable.",
            "images": [
                {"src": IMG("menuiserie", "accessoirs1.png"), "alt": "Accessoires menuiserie aluminium"},
                {"src": IMG("menuiserie", "acessoire3.png"), "alt": "Accessoires menuiserie aluminium"},
                {"src": IMG("menuiserie", "acessoires2.png"), "alt": "Accessoires menuiserie aluminium"},
            ],
        },
        {
            "type": "cta-banner",
            "title": "Un projet de menuiserie aluminium ?",
            "text": "Fenêtres, façades ou vérandas : nos équipes étudient votre demande sur-mesure.",
            "primary": {"label": "Demander un devis", "href": "contact.html"},
        },
    ],
})

def men_subpage(slug, title, hero_title, hero_lead, img_dir_items, extra_split=None, gallery_title=None):
    sections = []
    if extra_split:
        sections.append(extra_split)
    gallery_images = [{"src": IMG("menuiserie", f), "alt": title} for f in img_dir_items]
    sections.append({
        "type": "gallery",
        "eyebrow": "En images",
        "title": gallery_title or f"La gamme <span>{title}</span>",
        "images": gallery_images,
        "big_indexes": [0] if len(gallery_images) >= 5 else [],
    })
    sections.append({
        "type": "cta-banner",
        "title": f"Un projet « {title} » ?",
        "text": "Décrivez-nous votre besoin, nous revenons vers vous avec un devis adapté.",
        "primary": {"label": "Demander un devis", "href": "contact.html"},
    })
    add({
        "slug": slug, "template": "inner", "title": title,
        "description": f"{title} : menuiserie aluminium ASCO. {hero_lead}",
        "cat_nav": {**MEN_CAT_NAV, "active": slug},
        "hero": {
            "image": IMG("menuiserie", img_dir_items[0]),
            "eyebrow": "Menuiserie Aluminium",
            "title": hero_title,
            "lead": hero_lead,
            "breadcrumb": [("Accueil", "index.html"), ("Menuiserie Aluminium", "menuiserie-aluminium.html"), (title, slug)],
        },
        "sections": sections,
    })

men_subpage(
    "ouvrages-sur-paumelles.html", "Ouvrages sur paumelles",
    "Les <span>Ouvrages</span> sur Paumelles",
    "De belles portes et fenêtres contribuent au charme de la maison et à ses qualités de construction : elles rythment la façade et transforment la plus petite ouverture en véritable source de lumière.",
    ["ouvr-paumelle.jpg", "ouvr-paum.jpg", "paumelle.jpg"],
    extra_split={
        "type": "split",
        "eyebrow": "Nos modèles",
        "title": "Porte à la française, baie fixe ou <span>oscillo-battant</span>",
        "paragraphs": [
            "Une porte sur paumelle à la française : la menuiserie vous offre un large choix avec des ouvrages simples ou avec grille, moustiquaire, ou les deux à la fois. Aujourd'hui, la tendance est à la paumelle ou charnière invisible, à déterminer selon le poids de la porte, le modèle et sa finition.",
            "La baie vitrée fixe ne s'ouvre pas : souvent utilisée pour des fenêtres inaccessibles, elle apporte luminosité et esthétique à votre intérieur.",
            "La fenêtre oscillo-battante (ou vasistas) propose un double système d'ouverture à la française et à soufflet, qui répond à des impératifs d'aération mais aussi de sécurité pour les enfants.",
        ],
        "image": IMG("menuiserie", "paumelle.jpg"),
    },
)

men_subpage(
    "ouvrages-coulissants.html", "Ouvrages coulissants",
    "Les <span>Ouvrages</span> Coulissants",
    "Disponibles dans une grande variété de compositions, nos ouvrages coulissants assurent étanchéité, économies d'énergie et confort.",
    ["ouvr-coulis.jpg", "ouvr-coulis1.jpg", "ouvr-coulis2.jpg"],
    extra_split={
        "type": "split",
        "eyebrow": "Gain d'espace",
        "title": "Des portes coulissantes qui <span>libèrent l'espace</span>",
        "paragraphs": [
            "Elles apportent une véritable plus-value dans la rénovation ou la construction d'une maison : elles font gagner des mètres carrés en supprimant les débattements des portes, et la circulation devient plus fluide. La menuiserie vous offre un large choix avec des ouvrages simples ou avec grille, moustiquaire, ou les deux à la fois.",
            "La baie vitrée fixe par galandage n'empiète pas sur le volume de la pièce : vous profitez pleinement de vos espaces grâce à des ouvertures allant de 50 % à 100 %.",
        ],
        "image": IMG("menuiserie", "ouvr-coulis1.jpg"),
    },
)

men_subpage(
    "stores.html", "Stores",
    "Les <span>Stores</span>",
    "Les modèles de notre gamme de stores intérieurs ont été sélectionnés pour leur capacité à occulter la lumière, lutter contre le soleil ou la chaleur, en créant une atmosphère agréable dans votre intérieur.",
    ["store1.jpg", "stores2.jpg", "stores3.jpg"],
    extra_split={
        "type": "split",
        "eyebrow": "Deux univers",
        "title": "Stores vénitiens et <span>stores californiens</span>",
        "paragraphs": [
            "Le store vénitien, en bois ou aluminium, c'est le parfait contrôle de la lumière, l'élégance du design, voir sans être vu. Composé de lamelles horizontales, il préserve votre intimité grâce aux multiples possibilités d'orientation qui permettent de gérer et moduler la lumière, en l'occultant ou en la laissant diffuser.",
            "Le store à bandes verticales, ou store californien, est le store déco par excellence. Il s'adapte parfaitement aux fenêtres de grandes dimensions, portes et baies vitrées, et peut être couplé avec un store vénitien bois pour un rendu décoratif complet.",
        ],
        "image": IMG("menuiserie", "stores2.jpg"),
    },
)

men_subpage(
    "facades.html", "Façades",
    "Les <span>Façades</span>",
    "Face extérieure d'un bâtiment, la façade peut être réalisée en verre simple, double, triple, armé, feuilleté ou innovant. ASCO vous propose une large gamme selon vos moyens et vos attentes.",
    ["facade.jpg", "facade1.png", "facade3.jpg", "facade4.jpg"],
    extra_split={
        "type": "split",
        "eyebrow": "Murs rideaux",
        "title": "Chaque façade est <span>unique</span>",
        "paragraphs": [
            "Le nombre de vitres, l'épaisseur, l'espacement, le type de verre et les revêtements spéciaux font que chaque façade est différente. En mur rideau vitré, fibre de ciment ou panneau Alucobond, nos façades allient finition irréprochable et intégration à toute architecture.",
        ],
        "image": IMG("menuiserie", "facade3.jpg"),
    },
)

men_subpage(
    "rampes.html", "Rampes",
    "Les <span>Rampes</span>",
    "Élément décoratif autant que sécuritaire lors de la conception d'un escalier, la rampe est indispensable en présence d'enfants ou de personnes âgées.",
    ["rampes.jpg", "rampes1.jpg", "rampes3.jpg"],
    extra_split={
        "type": "split",
        "eyebrow": "Sécurité & design",
        "title": "Les rampes <span>d'escalier</span>",
        "paragraphs": [
            "La pose d'une rampe n'est pas obligatoire, mais elle devient indispensable dès que l'escalier est raide ou fréquenté par des enfants ou des personnes âgées : elle limite les sensations de vertige, de déséquilibre et d'insécurité tout en restant un élément décoratif à part entière.",
        ],
        "image": IMG("menuiserie", "rampes1.jpg"),
    },
)

men_subpage(
    "vitrages.html", "Vitrages",
    "Les <span>Vitrages</span>",
    "Simple, double, triple, armé, feuilleté ou innovant : une large gamme de vitrages en fonction de vos attentes en matière d'esthétique, d'acoustique et de sécurité.",
    ["vitrage.jpg", "vitrage1.jpg", "vitrage2.jpg", "vitrage3.jpg"],
    extra_split={
        "type": "split",
        "eyebrow": "Trois univers",
        "title": "Acoustique, anti-effraction, <span>blindé</span>",
        "paragraphs": [
            "Le vitrage acoustique réduit les pointes de résonance grâce à un double vitrage asymétrique : l'épaisseur des deux vitres et leur espacement adéquat assurent une isolation phonique performante, renforcée par l'usage d'un vitrage feuilleté.",
            "Le vitrage anti-effraction compte parmi les vitrages de sécurité qui permettent de prévenir ou retarder toute intrusion : un double vitrage avec vitres épaisses et films superposés peut résister à une trentaine de coups de masse avant de céder.",
            "Chaque vitrage blindé est élaboré pièce par pièce et sur-mesure, pour répondre aux demandes les plus exigeantes en matière de protection.",
        ],
        "image": IMG("menuiserie", "vitrage1.jpg"),
    },
)

# ================================================ OUVERTURES AUTO (cat) =====
AUTO_CAT_NAV = {"title": "Ouvertures Automatisées", "overview_href": "ouvertures-automatisees.html", "cards": NAV["automatisation"]}

add({
    "slug": "ouvertures-automatisees.html",
    "template": "inner",
    "title": "Ouvertures Automatisées",
    "description": "Portails coulissants, à battants, portes automatiques, barrières de parking, rideaux métalliques et bornes escamotables : l'automatisation ASCO pour l'habitat, le collectif et l'industriel.",
    "hero": {
        "image": IMG("hero", "ouvert-auto-1.jpg"),
        "eyebrow": "Métier n°2",
        "title": "Les <span>Ouvertures</span> Automatisées",
        "lead": "Un peu de temps pour soi est un bien qui n'a pas de prix. Automatiser certaines fonctions pratiques, c'est libérer du temps pour ce que nous aimons le plus.",
        "cta": {"label": "Demander un devis", "href": "contact.html"},
        "breadcrumb": [("Accueil", "index.html"), ("Ouvertures Automatisées", "ouvertures-automatisees.html")],
    },
    "sections": [
        {
            "type": "split",
            "eyebrow": "Pourquoi automatiser",
            "title": "Un temps précieux, <span>rendu</span> au quotidien",
            "paragraphs": [
                "Automatiser certaines fonctions pratiques signifie améliorer la vie quotidienne en libérant du temps à consacrer à ce que nous aimons le plus : une activité, une personne, ou simplement soi-même.",
                "Résidentiel, collectif ou industriel : ASCO dispose d'une gamme complète de motorisations adaptées à chaque configuration de portail, de porte ou de barrière.",
            ],
            "bullets": [
                "Moteurs 12V, 24V, 230V ou 400V triphasé selon l'usage",
                "Versions avec encodeur, sécurité renforcée",
                "Kits prêts à poser pour portails coulissants, battants et garages sectionnels",
            ],
            "image": IMG("hero", "ouvert-auto-2.jpg"),
            "badge": {"icon": "gate", "text": "Résidentiel & industriel"},
        },
        {
            "type": "category-grid", "bg": "alt", "cols": 3,
            "eyebrow": "Notre gamme",
            "title": "Choisissez votre <span>système</span>",
            "cards": [
                {"image": IMG("automatisation", "portailcoulissant.jpg"), "title": "Portails coulissants", "text": "300 kg à 4000 kg.", "href": "portails-coulissants.html"},
                {"image": IMG("automatisation", "portailabattant.jpg"), "title": "Portails à battants", "text": "Jusqu'à 5 m par vantail.", "href": "portails-a-battants.html"},
                {"image": IMG("automatisation", "portails-de-garage-sectionnelle.jpg"), "title": "Portails de garages sectionnelles", "text": "Motorisation sur-mesure.", "href": "portails-garages-sectionnelles.html"},
                {"image": IMG("automatisation", "portescoulissantauto3.jpg"), "title": "Portes coulissantes automatiques", "text": "Commerces et bâtiments publics.", "href": "portes-coulissantes-automatiques.html"},
                {"image": IMG("automatisation", "portes-sur-paumelle.jpg"), "title": "Portes sur paumelles automatiques", "text": "Bureaux, hôpitaux, collectivités.", "href": "portes-sur-paumelles-automatiques.html"},
                {"image": IMG("automatisation", "barreservparking.jpg"), "title": "Barrières & réservation de parking", "text": "Passage intense, usage intensif.", "href": "barriere-reservation-parking.html"},
                {"image": IMG("automatisation", "bornes-escamotables2.jpg"), "title": "Bornes escamotables", "text": "Gestion des accès véhicules.", "href": "bornes-escamotables.html"},
                {"image": IMG("automatisation", "rideaumetallique.jpg"), "title": "Rideaux métalliques & vasistas", "text": "Jusqu'à 8 m de hauteur.", "href": "rideaux-metalliques-vasistas.html"},
                {"image": IMG("automatisation", "acessoires.jpg"), "title": "Accessoires", "text": "Commandes, sécurité, énergie solaire.", "href": "accessoires.html"},
            ],
        },
        {
            "type": "cta-banner",
            "title": "Un portail ou une porte à automatiser ?",
            "text": "Nous étudions votre configuration et vous recommandons la motorisation la plus fiable.",
            "primary": {"label": "Demander un devis", "href": "contact.html"},
        },
    ],
})

def auto_subpage(slug, title, hero_title, hero_lead, intro_paragraphs, images, ranges=None, gallery_title=None):
    sections = [{
        "type": "split",
        "eyebrow": "Présentation",
        "title": f"L'automatisme <span>{title}</span>",
        "paragraphs": intro_paragraphs,
        "image": images[0] if images else IMG("hero", "ouvert-auto-3.png"),
    }]
    if images:
        sections.append({
            "type": "gallery",
            "eyebrow": "En images",
            "title": gallery_title or "Réalisations & produits",
            "images": [{"src": i, "alt": title} for i in images],
            "big_indexes": [0] if len(images) >= 5 else [],
        })
    if ranges:
        sections.append({
            "type": "range-grid",
            "eyebrow": "Nos séries",
            "title": "Caractéristiques <span>importantes</span>",
            "cards": ranges,
        })
    sections.append({
        "type": "cta-banner",
        "title": f"Un projet « {title} » ?",
        "text": "Dites-nous-en plus sur votre portail ou votre site : nous revenons vers vous avec une solution.",
        "primary": {"label": "Demander un devis", "href": "contact.html"},
    })
    add({
        "slug": slug, "template": "inner", "title": title,
        "description": f"{title} : ouvertures automatisées ASCO. {hero_lead}",
        "cat_nav": {**AUTO_CAT_NAV, "active": slug},
        "hero": {
            "image": images[0] if images else IMG("hero", "ouvert-auto-3.png"),
            "eyebrow": "Ouvertures Automatisées",
            "title": hero_title,
            "lead": hero_lead,
            "breadcrumb": [("Accueil", "index.html"), ("Ouvertures Automatisées", "ouvertures-automatisees.html"), (title, slug)],
        },
        "sections": sections,
    })

auto_subpage(
    "portails-coulissants.html", "Portails coulissants",
    "<span>Portails</span> Coulissants",
    "Une gamme de produits moderne et innovante, pour portails coulissants allant de 300 kg à 4000 kg.",
    ["Parmi les différents systèmes proposés par ASCO, le choix du moteur de portail coulissant est déterminé en fonction de votre portail et du type d'utilisation : résidentielle, collective ou industrielle.",
     "Selon la configuration de votre portail, la fréquence de passage (élevée ou faible) et l'utilisation globale souhaitée, nous vous orientons vers le modèle le plus adapté."],
    [IMG("automatisation", "portailcoulissant.jpg"), IMG("automatisation", "portailcoulissant1.jpg"), IMG("automatisation", "portailcoulissant2.jpg"), IMG("automatisation", "portailcoulissant3.jpg"), IMG("automatisation", "portailcoulissant4.jpg"), IMG("automatisation", "portailcoulissant6.jpg"), IMG("automatisation", "portailcoulissant7.jpg")],
    ranges=[
        {"name": "Série T-ONE", "tag": "Résidentiel / collectif", "weight": "300 à 1200 kg", "voltage": "12V · 24V · 230V", "text": "Gamme complète pour automatiser des portails coulissants à usage résidentiel et collectif, disponible en 3 versions."},
        {"name": "Série MASTER", "tag": "Collectif / industriel", "weight": "1200 à 2000 kg", "voltage": "12V · 230V · 400V", "text": "Motoréducteur électromécanique pour portails coulissants à usage collectif ou industriel."},
        {"name": "Série BIG", "tag": "Industriel lourd", "weight": "2500 à 4000 kg", "voltage": "400V triphasé", "text": "Pour les portails coulissants les plus lourds, uniquement disponible en 400 Volts triphasé."},
    ],
)

auto_subpage(
    "portails-a-battants.html", "Portails à battants",
    "<span>Portails</span> à Battants",
    "Au sein de notre large gamme d'automatismes de portails, ASCO dispose de nombreux systèmes de motorisation pour portails à battants allant de 3 m à 5 m par vantail.",
    ["Léger ou lourd, en version 12 à 230 Volts avec encodeur : quel que soit votre style et les matériaux utilisés (bois, PVC, fer forgé…), les dimensions et le poids de votre portail à battant, nous vous proposons la solution d'automatisme qui vous conviendra le mieux."],
    [IMG("automatisation", "portailabattant.jpg"), IMG("automatisation", "portailabattant1.jpg"), IMG("automatisation", "portailabattant3.jpg"), IMG("automatisation", "portailabattant4.jpg"), IMG("automatisation", "portailabattant5.jpg"), IMG("automatisation", "portailabattant6.jpg"), IMG("automatisation", "portailabattant7.jpg"), IMG("automatisation", "portailabattant8.jpg")],
    ranges=[
        {"name": "Série ARM200", "tag": "Vérin électromécanique", "voltage": "12V ou 230V", "text": "Vérin électromécanique à sortie tige, 6 versions pour battants allant jusqu'à 5 m par vantail, avec encodeur."},
        {"name": "Série ARM2000", "tag": "Vérin électromécanique", "voltage": "12V ou 230V", "text": "Vérin électromécanique à sortie tige, 6 versions pour battants allant jusqu'à 5 m par vantail, avec encodeur."},
        {"name": "Série EASY", "tag": "Bras articulé", "voltage": "12V ou 230V", "text": "Motoréducteur à bras articulé pour battants de 2,3 m ou 3,5 m, encombrement réduit, idéal pour piliers de grandes dimensions."},
        {"name": "Série ZIP", "tag": "Bras articulé", "voltage": "12V ou 230V", "text": "Motoréducteur à bras articulé pour battants de 2,3 m ou 3,5 m, encombrement réduit, idéal pour piliers de grandes dimensions."},
    ],
)

auto_subpage(
    "portails-garages-sectionnelles.html", "Portails de garages sectionnelles",
    "Portails de <span>Garages</span> Sectionnelles",
    "Au sein de notre large gamme d'automatismes de portails, ASCO motorise également les portails de garages sectionnels, pour un usage résidentiel comme collectif.",
    ["Quel que soit le style et les matériaux utilisés, les dimensions et le poids de votre portail sectionnel, nous vous proposons la solution d'automatisme la mieux adaptée à votre installation."],
    [IMG("automatisation", "portails-de-garage-sectionnelle.jpg"), IMG("automatisation", "portesdegaragessectionnelles.jpg")],
)

auto_subpage(
    "portes-coulissantes-automatiques.html", "Portes coulissantes automatiques",
    "Portes <span>Coulissantes</span> Automatiques",
    "À usage commercial ou intensif, idéal pour les commerces, supermarchés et bâtiments publics : des opérateurs pour portes coulissantes à un ou deux vantaux mobiles.",
    ["Longueur maximum de 6 m et poids allant jusqu'à 150 kg par vantail. Selon l'ouverture désirée (centrale ou télescopique rectiligne, 1+1 ou 2+2 vantaux), nous sommes à votre disposition."],
    [IMG("automatisation", "portescoulissantauto3.jpg"), IMG("automatisation", "portescoulissantauto4.jpg")],
    ranges=[
        {"name": "Série DOOR", "tag": "Usage intensif", "text": "Automatisme pour portes coulissantes à usage rapide et intensif."},
        {"name": "Série BLOW", "tag": "Télescopique", "text": "Automatisme pour portes coulissantes télescopiques rectilignes."},
    ],
)

auto_subpage(
    "portes-sur-paumelles-automatiques.html", "Portes sur paumelles automatiques",
    "Portes sur <span>Paumelles</span> Automatiques",
    "À usage commercial ou intensif : idéal pour les bureaux à passage intense, les supermarchés, les hôpitaux ou les collectivités.",
    ["Des opérateurs pour porte battante équipant un ou deux vantaux de longueur maximum 1,40 m et d'un poids allant jusqu'à 250 kg par vantail. Installation facile, sans modifier la porte, avec des bras articulés à pousser ou à tirer."],
    [IMG("automatisation", "portes-sur-paumelle.jpg"), IMG("automatisation", "portes-sur-paumelle1.jpg")],
    ranges=[
        {"name": "Série BRINK", "tag": "Bras articulé", "weight": "jusqu'à 250 kg", "text": "Automatisme pour portes à battants, jusqu'à 250 kg pour un vantail de 1400 mm."},
    ],
)

auto_subpage(
    "barriere-reservation-parking.html", "Barrières & réservation de parking",
    "Barrières & <span>Réservation</span> de Parking",
    "Des barrières automatiques basse tension et des dispositifs de réservation de place, pour les parkings à passage intense.",
    ["Structure laquée, lisse télescopique en aluminium droite ou flexible, à usage résidentiel, industriel ou collectif. Fonctionnement assuré en cas de coupure de courant grâce à des batteries de secours."],
    [IMG("automatisation", "barreservparking.jpg"), IMG("automatisation", "barreservparking1.jpg"), IMG("automatisation", "barreservparking2.jpg"), IMG("automatisation", "barreservparking3.jpg")],
    ranges=[
        {"name": "Barrières", "tag": "4 à 6 m", "text": "Barrière automatique basse tension, ouverture de passage utile de 4 à 6 m, fonctionnement assuré même en coupure de courant."},
        {"name": "Réservation de parking", "tag": "Ouverture 5 s", "text": "Dispositif de réservation de parking automatique basse tension, ouverture en 5 secondes, commande par émetteur ou manuelle."},
    ],
)

auto_subpage(
    "rideaux-metalliques-vasistas.html", "Rideaux métalliques & vasistas",
    "Rideaux <span>Métalliques</span> & Vasistas",
    "Des motoréducteurs fiables pour rideaux métalliques et fenêtres vasistas, sans entretien nécessaire.",
    ["Nos rideaux métalliques montent jusqu'à 8 m de hauteur, avec une force de levage allant jusqu'à 320 kg, adaptables à différents diamètres de tuyaux d'enroulement et de ressorts."],
    [IMG("automatisation", "rideaumetallique.jpg"), IMG("automatisation", "rideaumetallique2.jpg"), IMG("automatisation", "rideaumetallique3.jpg"), IMG("automatisation", "rideaumetallique4.jpg"), IMG("automatisation", "vasistas.jpg"), IMG("automatisation", "vasistas1.jpg"), IMG("automatisation", "vasistas2.jpg")],
    ranges=[
        {"name": "Rideaux métalliques", "tag": "Jusqu'à 8 m", "weight": "jusqu'à 320 kg", "text": "Motoréducteur solide et fiable, aucun entretien nécessaire, adaptable à de nombreux diamètres de tuyaux et ressorts."},
        {"name": "Opérateur MF", "tag": "Vasistas", "weight": "jusqu'à 30 kg", "text": "Moteur à chaîne articulée à double maillon pour fenêtre vasistas ou en saillie."},
    ],
)

auto_subpage(
    "bornes-escamotables.html", "Bornes escamotables",
    "Les <span>Bornes</span> Escamotables",
    "La réponse idéale aux besoins des utilisateurs privés et de l'administration publique : centres d'affaires, chaînes de supermarchés, concessionnaires automobiles, centres historiques.",
    ["Là où l'élégance ne peut négliger ni la sécurité ni l'intégrité du public, la borne escamotable organise la circulation urbaine, contrôle et gère les accès pour véhicules, délimite des zones sensibles et prévient le stationnement interdit."],
    [IMG("automatisation", "borne-escamotable1.jpg"), IMG("automatisation", "bornes-escamotables2.jpg"), IMG("automatisation", "bornes-escamotables3.jpg"), IMG("automatisation", "bornes-escamotables4.jpg")],
)

auto_subpage(
    "accessoires.html", "Accessoires",
    "<span>Accessoires</span> d'Ouverture Automatisée",
    "Télécommandes, commandes à clé, détecteurs et énergie solaire : le supplément parfait pour votre installation.",
    ["Nos télécommandes offrent un riche panel de fonctionnalités pour contrôler votre portail automatique coulissant, battant, ou vos portes automatisées : commandes radio basique ou programmable, intégrant des technologies d'encodage du signal pour éviter les interférences.",
     "Les commandes à clé magnétique ou clavier numérique résistent aux intempéries et aux effractions grâce à leur structure en acier ou en aluminium. Couplées à nos dispositifs automatiques, elles permettent de contrôler l'accès à un parking ou à votre domicile."],
    [IMG("automatisation", "acessoires.jpg"), IMG("automatisation", "acessoires1.jpg"), IMG("automatisation", "acessoires3.jpg")],
    ranges=[
        {"name": "Commandes radio", "tag": "433,92 MHz", "text": "Transmetteurs radio multi-canaux et multi-utilisateurs pour chaque type d'application, large choix d'émetteurs et de récepteurs."},
        {"name": "Sélecteurs à clé & clavier", "tag": "Accès", "text": "Sélecteurs de commande à clé, numériques, et capteurs pour cartes transpondeur."},
        {"name": "Clavier numérique radio", "tag": "Autonome", "text": "Clavier numérique à pile fonctionnant par radio."},
        {"name": "Sécurité mouvement", "tag": "Détection", "text": "Clignotants de mouvement, photocellules à rayon infrarouge et bords sensibles de sécurité."},
        {"name": "Kit solaire", "tag": "Énergie", "text": "Kit panneau photovoltaïque de 50 ou 90 Watt, avec carte de réglage et batterie 27 Ah."},
        {"name": "Détecteur de proximité", "tag": "Contrôle d'accès", "text": "Détecteur de transpondeur de proximité pour contrôle d'accès, jusqu'à 80 utilisateurs."},
    ],
)

# ======================================================= SOLUTIONS D'ACCES ==
add({
    "slug": "solutions-dacces.html",
    "template": "inner",
    "title": "Solutions d'Accès",
    "description": "Serrures électroniques, cylindres sur organigramme, contrôle d'accès industriel et véhicules : les solutions d'accès ASCO pour votre sécurité.",
    "hero": {
        "image": IMG("hero", "paddedimage723390-serrure.jpg"),
        "eyebrow": "Métier n°3",
        "title": "Les <span>Solutions</span> d'Accès",
        "lead": "ASCO, le partenaire idéal pour votre sécurité dans la gestion des accès : résidentiel, professionnel ou industriel.",
        "cta": {"label": "Demander un devis", "href": "contact.html"},
        "breadcrumb": [("Accueil", "index.html"), ("Solutions d'Accès", "solutions-dacces.html")],
    },
    "sections": [
        {
            "type": "split",
            "eyebrow": "Le partenaire idéal",
            "title": "Pour votre <span>sécurité</span>, personnelle et professionnelle",
            "paragraphs": [
                "Vous êtes à la recherche d'un partenaire compétent pouvant répondre à vos exigences personnelles et professionnelles de sécurité dans le domaine de la gestion des accès, un partenaire qui comprenne vos besoins, dispose de solutions flexibles et puisse vous suivre partout ? ASCO est ce partenaire, appuyé par un réseau international de sécurité.",
                "Du résidentiel au secteur industriel, en passant par les bureaux, commerces et établissements hôteliers, qu'ils soient à codes, à cartes ou à empreinte digitale, qu'ils soient de simples clés ou sécurisés à vie : nous proposons une large gamme de cylindres, de batteuses, de cadenas et d'autres produits combinés qui capitalisent et exploitent l'ensemble des informations mises en mémoire pour audit.",
            ],
            "image": IMG("solutions-acces", "sol-access-1-.jpg"),
            "badge": {"icon": "key", "text": "Résidentiel · Professionnel · Industriel"},
        },
        {
            "type": "split", "reverse": True, "bg": "alt",
            "eyebrow": "Nos systèmes exclusifs",
            "title": "MESSENGER, <span>EXOS</span>, SMARTAIR",
            "paragraphs": [
                "Quel que soit votre secteur, découvrez l'exclusivité de nos systèmes qui font mouche : MESSENGER pour l'hôtellerie, EXOS pour vos sites industriels, SMARTAIR pour les administrations et les habitations.",
                "Ils interviennent sur vos sites dans la gestion des visiteurs, le contrôle d'accès de tous les types de portes et de parkings de véhicules, la gestion du personnel, la gestion du temps, et au-delà.",
                "Nous accompagnons tous nos produits avec des accessoires complémentaires : cartes, badges, coffres-forts, économiseurs d'énergie, horodateurs de présence, logiciels, etc.",
            ],
            "image": IMG("solutions-acces", "sol-access-3-.jpg"),
        },
        {
            "type": "gallery", "id": "hotelier", "bg": "alt",
            "eyebrow": "Hôtelier",
            "title": "Serrures à cartes et <span>lecteurs hôteliers</span>",
            "lead": "Serrures à cartes, autres lecteurs, accessoires et système Messenger pour l'hôtellerie et la para-hôtellerie.",
            "images": [
                {"src": IMG("solutions-acces", "sol-access-7-.jpg"), "alt": "Serrures hôtelières en situation"},
                {"src": IMG("solutions-acces", "sol-access-1-.jpg"), "alt": "Serrures hôtelières à carte"},
                {"src": IMG("solutions-acces", "sol-access-2-.jpg"), "alt": "Solutions d'accès hôtelier"},
                {"src": IMG("solutions-acces", "sol-access-4-.jpg"), "alt": "Solutions d'accès hôtelier"},
                {"src": IMG("solutions-acces", "sol-access-9-.jpg"), "alt": "Serrures hôtelières Orbita"},
            ],
            "big_indexes": [0],
        },
        {
            "type": "gallery", "id": "industriel",
            "eyebrow": "Industriel",
            "title": "EXOS & <span>Smartair</span>",
            "lead": "Des solutions de contrôle d'accès pensées pour les sites industriels et les administrations.",
            "images": [
                {"src": IMG("divers", "accessoircontrol1-1.jpg"), "alt": "Contrôle d'accès industriel"},
                {"src": IMG("divers", "accessoircontrol1-2.jpg"), "alt": "Contrôle d'accès industriel"},
                {"src": IMG("divers", "accessoircontrol1-3.jpg"), "alt": "Contrôle d'accès industriel"},
                {"src": IMG("divers", "accessoircontrol1-4.jpg"), "alt": "Contrôle d'accès industriel"},
            ],
        },
        {
            "type": "feature-grid", "id": "organigramme", "bg": "alt", "cols": 4,
            "eyebrow": "Clés sur organigramme",
            "title": "Une organisation <span>sur-mesure</span> de vos clés",
            "lead": "Du cylindre simple au système hiérarchisé, maîtrisez qui ouvre quoi, à chaque niveau de votre bâtiment.",
            "cards": [
                {"icon": "key", "title": "Cylindre simple et sécurisé", "text": "Solution économique pour un usage courant et fiable."},
                {"icon": "key", "title": "Combinaison cylindre et autres", "text": "Des combinaisons multiples pour des besoins spécifiques."},
                {"icon": "shield", "title": "Cylindre de haute sécurité", "text": "Protection renforcée contre le crochetage et la copie."},
                {"icon": "shield", "title": "Mortaises de sécurité", "text": "Renforts de porte pour une résistance maximale à l'effraction."},
            ],
        },
        {
            "type": "feature-grid", "id": "vehicules", "cols": 3,
            "eyebrow": "Autres gammes",
            "title": "Véhicules, <span>cylindres</span> & systèmes complémentaires",
            "cards": [
                {"icon": "gate", "title": "Véhicules", "text": "Solutions d'accès et de sécurisation pour flottes et parkings."},
                {"icon": "key", "title": "Gamme Génération, Quantum & MT", "text": "Nos familles de cylindres mécaniques et digitaux."},
                {"icon": "safe", "title": "Accessoires complémentaires", "text": "Clés multifonctions, systèmes d'encodage professionnels et plus."},
            ],
        },
        {
            "type": "cta-banner",
            "title": "Sécuriser l'accès à votre établissement ?",
            "text": "Commerce, site industriel ou résidence : nous construisons avec vous la solution adaptée.",
            "primary": {"label": "Demander un devis", "href": "contact.html"},
            "secondary": {"label": "Voir les coffres-forts", "href": "coffre-fort.html"},
        },
    ],
})

# ============================================================ COFFRE-FORT ===
add({
    "slug": "coffre-fort.html",
    "template": "inner",
    "title": "Coffres-forts",
    "description": "Coffres-forts électroniques pour particuliers et professionnels, armoires fortes, coffres de haute sécurité et solutions sur-mesure, par ASCO Groupe.",
    "hero": {
        "image": IMG("coffre-fort", "coffre-fort1.jpg"),
        "eyebrow": "Sécurité & confort",
        "title": "Les <span>Coffres-forts</span>",
        "lead": "Une meilleure sécurité pour vos biens, à la maison, au bureau ou en déplacement.",
        "cta": {"label": "Demander un devis", "href": "contact.html"},
        "breadcrumb": [("Accueil", "index.html"), ("Coffres-forts", "coffre-fort.html")],
    },
    "sections": [
        {
            "type": "split",
            "eyebrow": "Conçus pour rassurer",
            "title": "Sécurité, fiabilité et <span>simplicité</span> d'utilisation",
            "paragraphs": [
                "De nos jours, particuliers et professionnels ont des biens à protéger : caméscopes, ordinateurs portables, bijoux, documents… À la maison, au bureau ou à l'hôtel, un coffre-fort fiable est devenu indispensable.",
                "Les coffres-forts électroniques ASCO sont conçus dans un esprit de sécurité, de fiabilité, de confort et de simplicité d'utilisation, pour sécuriser au maximum les objets de vos clients.",
            ],
            "bullets": [
                "Coffres pour particuliers et bureaux", "Armoires fortes", "Coffres de haute sécurité", "Chambres d'hôtel électroniques",
            ],
            "image": IMG("coffre-fort", "coffre-fort5.jpg"),
            "badge": {"icon": "safe", "text": "Sur-mesure disponible"},
        },
        {
            "type": "feature-grid", "bg": "alt", "cols": 4,
            "eyebrow": "Notre gamme",
            "title": "Un coffre pour <span>chaque usage</span>",
            "cards": [
                {"icon": "safe", "title": "Particuliers", "text": "Des modèles adaptés à la maison et au bureau."},
                {"icon": "safe", "title": "Domestique", "text": "Format compact pour un usage résidentiel quotidien."},
                {"icon": "building", "title": "Armoires fortes", "text": "Pour la protection de documents et valeurs en volume."},
                {"icon": "shield", "title": "Haute sécurité", "text": "Protection renforcée contre effraction et incendie."},
                {"icon": "safe", "title": "Dépôt Protect", "text": "Dépôt sécurisé sans réouverture, idéal commerces."},
                {"icon": "building", "title": "Colonne Protect", "text": "Solution verticale gain de place pour sites sensibles."},
                {"icon": "safe", "title": "Chambres d'hôtel électroniques", "text": "Compacts et simples d'usage, pour l'hôtellerie."},
                {"icon": "key", "title": "Accessoires", "text": "Serrures, piles et équipements complémentaires."},
            ],
        },
        {
            "type": "gallery",
            "eyebrow": "En images",
            "title": "Notre <span>gamme</span> de coffres-forts",
            "images": [
                {"src": IMG("coffre-fort", "coffre-fort1.jpg"), "alt": "Coffre-fort électronique"},
                {"src": IMG("coffre-fort", "ccoffre-fort.jpg"), "alt": "Coffre-fort"},
                {"src": IMG("coffre-fort", "coffre-fort-4.jpg"), "alt": "Coffre-fort"},
                {"src": IMG("coffre-fort", "coffre-fort5.jpg"), "alt": "Coffre-fort"},
                {"src": IMG("coffre-fort", "coffre-fort6.jpg"), "alt": "Coffre-fort"},
            ],
            "big_indexes": [0],
        },
        {
            "type": "cta-banner",
            "title": "Vous ne trouvez pas le produit idéal ?",
            "text": "Nous sommes capables de réaliser du sur-mesure : tailles, coloris, serrures.",
            "primary": {"label": "Contactez-nous", "href": "contact.html"},
        },
    ],
})

# ============================================================== CONTACT ====
add({
    "slug": "contact.html",
    "template": "contact",
    "title": "Contact",
    "description": "Contactez ASCO Groupe à Cotonou : téléphone, email, WhatsApp ou formulaire de devis. Nous répondons rapidement à votre demande.",
    "hero": {
        "image": IMG("hero", "men-alum4.jpg"),
        "eyebrow": "Parlons de votre projet",
        "title": "Contactez-nous",
        "lead": "Une question, un devis, une urgence technique ? Notre équipe à Cotonou vous répond rapidement.",
        "breadcrumb": [("Accueil", "index.html"), ("Contact", "contact.html")],
    },
})
