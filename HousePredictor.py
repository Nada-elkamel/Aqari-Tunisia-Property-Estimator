

# import streamlit as st
# import pandas as pd
# import numpy as np
# import warnings
# import time

# warnings.filterwarnings("ignore")

# st.set_page_config(
#     page_title="Aqari · Tunisia Property Estimator",
#     page_icon="🏡",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# # ─────────────────────────────────────────────────────────────────
# # CSS
# # ─────────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

# :root {
#     --bg:        #080c14;
#     --surface:   #0e1421;
#     --card:      #111827;
#     --card2:     #0d1520;
#     --border:    #1e293b;
#     --gold:      #c9a84c;
#     --gold-lt:   #e8c96a;
#     --gold-dk:   #8a6a20;
#     --teal:      #0ea5c9;
#     --teal-lt:   #38c0e0;
#     --green:     #4ade80;
#     --text:      #e8edf5;
#     --text-muted:#7a8da8;
#     --text-dim:  #4a5a72;
# }

# html, body, [class*="css"] {
#     font-family: 'DM Sans', sans-serif;
#     color: var(--text);
#     background-color: var(--bg);
# }
# .stApp { background: var(--bg); }
# #MainMenu, footer, header { visibility: hidden; }
# [data-testid="stSidebar"] { display: none; }
# .block-container { padding: 2rem 2.5rem 3rem !important; max-width: 1500px; }

# [data-testid="stNumberInput"] input,
# .stTextInput input {
#     background: var(--card) !important;
#     border: 1px solid var(--border) !important;
#     border-radius: 8px !important;
#     color: var(--text) !important;
#     font-family: 'DM Mono', monospace !important;
#     font-size: 0.88rem !important;
#     padding: 0.5rem 0.75rem !important;
# }
# [data-testid="stNumberInput"] input:focus {
#     border-color: var(--gold) !important;
#     box-shadow: 0 0 0 2px rgba(201,168,76,0.15) !important;
# }

# [data-testid="stSelectbox"] > div > div {
#     background: var(--card) !important;
#     border: 1px solid var(--border) !important;
#     border-radius: 8px !important;
#     color: var(--text) !important;
#     font-family: 'DM Mono', monospace !important;
#     font-size: 0.88rem !important;
# }
# [data-testid="stSelectbox"] > div > div:hover { border-color: var(--gold-dk) !important; }

# [data-testid="stSlider"] > div > div > div > div {
#     background: linear-gradient(90deg, var(--gold-dk), var(--gold)) !important;
# }
# [data-testid="stSlider"] > div > div > div > div > div {
#     background: var(--gold) !important;
#     border: 2px solid var(--gold-lt) !important;
#     box-shadow: 0 0 10px rgba(201,168,76,0.5) !important;
# }

# [data-testid="stCheckbox"] > label > div:first-child {
#     background: var(--card) !important;
#     border-color: var(--border) !important;
#     border-radius: 4px !important;
# }
# [data-testid="stCheckbox"] > label > div[aria-checked="true"] {
#     background: var(--gold) !important;
#     border-color: var(--gold) !important;
# }
# [data-testid="stCheckbox"] label p { color: var(--text-muted) !important; font-size: 0.83rem !important; }

# .stButton > button {
#     background: linear-gradient(135deg, var(--gold-dk), var(--gold), var(--gold-lt)) !important;
#     color: #060a10 !important;
#     border: none !important;
#     border-radius: 10px !important;
#     font-family: 'DM Sans', sans-serif !important;
#     font-weight: 700 !important;
#     font-size: 1rem !important;
#     letter-spacing: 0.06em !important;
#     padding: 0.75rem 2rem !important;
#     transition: all 0.2s ease !important;
#     box-shadow: 0 4px 20px rgba(201,168,76,0.35) !important;
#     width: 100% !important;
# }
# .stButton > button:hover {
#     transform: translateY(-2px) !important;
#     box-shadow: 0 8px 32px rgba(201,168,76,0.55) !important;
# }

# hr { border-color: var(--border) !important; margin: 1.2rem 0 !important; }
# label { color: var(--text-muted) !important; font-size: 0.82rem !important; }
# .stMarkdown p { color: var(--text-muted) !important; font-size: 0.85rem; }

# [data-testid="stMetric"] {
#     background: var(--card2);
#     border: 1px solid var(--border);
#     border-radius: 12px;
#     padding: 0.9rem 1.1rem;
# }
# [data-testid="stMetric"] label { color: var(--text-muted) !important; font-size: 0.75rem !important; }
# [data-testid="stMetric"] [data-testid="stMetricValue"] {
#     color: var(--gold) !important;
#     font-family: 'Cormorant Garamond', serif !important;
#     font-size: 1.6rem !important;
#     font-weight: 600 !important;
# }

# [data-testid="stExpander"] {
#     background: var(--card) !important;
#     border: 1px solid var(--border) !important;
#     border-radius: 10px !important;
# }
# [data-testid="stExpander"] summary p { color: var(--text-muted) !important; font-size: 0.82rem !important; }

# .panel {
#     background: var(--card);
#     border: 1px solid var(--border);
#     border-radius: 14px;
#     padding: 1.6rem 1.8rem;
# }
# .panel-title {
#     font-family: 'Cormorant Garamond', serif;
#     font-size: 1.15rem;
#     font-weight: 600;
#     color: var(--gold);
#     letter-spacing: 0.1em;
#     text-transform: uppercase;
#     padding-bottom: 0.7rem;
#     border-bottom: 1px solid var(--border);
#     margin-bottom: 1.2rem;
# }
# .section-label {
#     font-family: 'DM Sans', sans-serif;
#     font-size: 0.72rem;
#     font-weight: 600;
#     color: var(--text-dim);
#     letter-spacing: 0.18em;
#     text-transform: uppercase;
#     margin: 1.2rem 0 0.5rem;
# }
# .result-card {
#     background: linear-gradient(135deg, #0c1525 0%, #111e32 100%);
#     border: 1px solid var(--gold-dk);
#     border-radius: 16px;
#     padding: 2.2rem 2rem;
#     text-align: center;
#     box-shadow: 0 0 50px rgba(201,168,76,0.07), inset 0 0 80px rgba(201,168,76,0.025);
#     margin-bottom: 1.5rem;
# }
# .price-display {
#     font-family: 'Cormorant Garamond', serif;
#     font-size: 3.8rem;
#     font-weight: 700;
#     background: linear-gradient(135deg, var(--gold-dk), var(--gold), var(--gold-lt));
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     background-clip: text;
#     line-height: 1.05;
#     letter-spacing: -0.02em;
# }
# .price-sub {
#     font-family: 'DM Mono', monospace;
#     font-size: 1.05rem;
#     color: var(--text-muted);
#     margin-top: 0.4rem;
# }
# .badge {
#     display: inline-block;
#     padding: 0.22rem 0.75rem;
#     border-radius: 20px;
#     font-size: 0.72rem;
#     font-weight: 500;
#     font-family: 'DM Mono', monospace;
#     letter-spacing: 0.05em;
#     text-transform: uppercase;
#     margin: 0.25rem 0.2rem;
# }
# .badge-gold  { background: rgba(201,168,76,0.12); color: var(--gold);    border: 1px solid rgba(201,168,76,0.28); }
# .badge-teal  { background: rgba(14,165,201,0.10); color: var(--teal-lt); border: 1px solid rgba(14,165,201,0.22); }
# .badge-green { background: rgba(74,222,128,0.10); color: var(--green);   border: 1px solid rgba(74,222,128,0.22); }
# .info-row {
#     display: flex; justify-content: space-between; align-items: center;
#     padding: 0.55rem 0; border-bottom: 1px solid var(--border); font-size: 0.83rem;
# }
# .info-row:last-child { border-bottom: none; }
# .info-label { color: var(--text-muted); }
# .info-value { color: var(--text); font-family: 'DM Mono', monospace; font-weight: 500; }
# .amenity-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.4rem; margin-top: 0.5rem; }
# .amenity-item {
#     display: flex; align-items: center; gap: 0.45rem;
#     font-size: 0.79rem; color: var(--text-muted);
#     padding: 0.35rem 0.55rem;
#     background: var(--surface); border-radius: 6px; border: 1px solid var(--border);
# }
# .amenity-item.active { color: var(--gold); border-color: rgba(201,168,76,0.28); background: rgba(201,168,76,0.04); }
# .placeholder-box {
#     text-align: center; padding: 5rem 2rem;
#     border: 1px dashed var(--border); border-radius: 16px; background: var(--card2);
# }
# .watermark {
#     font-family: 'Cormorant Garamond', serif; font-size: 0.72rem; color: var(--text-dim);
#     text-align: center; letter-spacing: 0.15em; text-transform: uppercase;
#     margin-top: 2.5rem; padding-top: 1rem; border-top: 1px solid var(--border);
# }
# </style>
# """, unsafe_allow_html=True)

# # ─────────────────────────────────────────────────────────────────
# # CONSTANTS
# # ─────────────────────────────────────────────────────────────────
# CITIES_BY_GOV = {
#     "Ariana":       ["Ariana Ville","Ettadhamen","Kalaat Landalous","La Soukra","Mnihla","Raoued","Sidi Thabet"],
#     "Ben Arous":    ["Ben Arous","Boumhel Bassatine","El Mourouj","Ezzahra","Fouchana","Hammam Chatt","Hammam Lif","Mohamadia","Mornag","Mégrine","Nouvelle Medina","Rades"],
#     "Bizerte":      ["Bizerte Nord","Bizerte Sud","Metline"],
#     "Béja":         ["Béja"],
#     "Djerba":       ["Ajim","Djerba","Houmt Souk","Midoun"],
#     "El Kasserine": ["El Kasserine"],
#     "Gabès":        ["Gabès Ville"],
#     "Gafsa":        ["Gafsa"],
#     "Jendouba":     ["Tabarka"],
#     "Kairouan":     ["Kairouan Ville"],
#     "Kébili":       ["Douz"],
#     "La Manouba":   ["Borj El Amri","Douar Hicher","El Battan","Jedaida","La Manouba","Mornaguia","Oued Ellil","Tebourba"],
#     "Le Kef":       ["Le Kef"],
#     "Mahdia":       ["Mahdia Ville"],
#     "Medenine":     ["Medenine"],
#     "Monastir":     ["Monastir Ville"],
#     "Nabeul":       ["Beni Khiar","Hammamet","Nabeul"],
#     "Sfax":         ["Menzel Chaker","Sakiet Eddaier","Sakiet Ezzit","Sfax Ouest","Sfax Sud","Sfax Ville"],
#     "Siliana":      ["Siliana"],
#     "Sousse":       ["Akouda","Hammam Sousse","Sousse Jaouhara","Sousse Riadh","Sousse Ville"],
#     "Tataouine":    ["Tataouine"],
#     "Zaghouan":     ["Zaghouan"],
#     "tunis":        ["Carthage","Cité El Khadra","El Hrairia","El Kabaria","El Menzah","El Omrane","El Omrane Superieur","El Ouardia","Ettahrir","La Goulette","La Marsa","Le Bardo","Le Kram","Sidi Hassine","Tunis"],
# }
# GOV_COORDS = {
#     "tunis":(36.82,10.17,2.0), "Ariana":(36.87,10.19,8.0),
#     "Ben Arous":(36.65,10.22,15.0), "La Manouba":(36.81,10.10,7.0),
#     "Nabeul":(36.45,10.73,65.0), "Sousse":(35.83,10.64,115.0),
#     "Monastir":(35.77,10.82,135.0), "Mahdia":(35.50,11.07,170.0),
#     "Sfax":(34.74,10.76,270.0), "Kairouan":(35.67,10.10,155.0),
#     "Bizerte":(37.27,9.87,60.0), "Béja":(36.73,9.18,90.0),
#     "Jendouba":(36.50,8.78,145.0), "Le Kef":(36.18,8.71,180.0),
#     "Siliana":(36.08,9.37,140.0), "Zaghouan":(36.40,10.14,55.0),
#     "Djerba":(33.87,10.85,330.0), "Gabès":(33.88,9.54,310.0),
#     "Medenine":(33.35,10.50,380.0), "Tataouine":(32.93,10.45,450.0),
#     "Kébili":(33.71,8.97,370.0), "Gafsa":(34.43,8.78,270.0),
#     "El Kasserine":(35.17,8.83,230.0),
# }

# # ─────────────────────────────────────────────────────────────────
# # MODEL
# # ─────────────────────────────────────────────────────────────────
# @st.cache_resource(show_spinner=False)
# def load_and_train():
#     from sklearn.experimental import enable_iterative_imputer  
#     from sklearn.impute import IterativeImputer, KNNImputer
#     from sklearn.preprocessing import LabelEncoder
#     from sklearn.linear_model import BayesianRidge
#     from sklearn.ensemble import HistGradientBoostingRegressor
#     from sklearn.model_selection import train_test_split
#     from sklearn.metrics import r2_score, mean_absolute_error

#     df = pd.read_csv("dataSetFull.csv")
#     df["governorate"] = df["governorate"].str.strip()
#     df.drop(columns=["price_eur","id"], inplace=True)

#     age_map = {"0":0,"1-5 ":3,"5-10 ":7.5,"10,20":15,"10-20 ":15,
#                "20-30 ":25,"30-50 ":40,"50-70 ":60,"70-100 ":85,"Plus de 100 ":110}
#     df["age_years"] = df["age"].map(age_map)
#     df.drop(columns=["age"], inplace=True)

#     amenity_cols = ["garage","garden","concierge","beach_view","mountain_view",
#                     "pool","elevator","furnished","equipped_kitchen","central_heating","air_conditioning"]
#     df["amenity_score"] = df[amenity_cols].sum(axis=1)
#     df["rooms_per_100m2"] = np.where((df["Area"].notna()) & (df["Area"]>0),
#                                      (df["room"]/df["Area"])*100, np.nan)

#     def winsorize(s, lo=0.01, hi=0.99):
#         return s.clip(s.quantile(lo), s.quantile(hi))

#     for col in ["price_tnd","Area","pieces","room","bathroom","distance_to_capital","age_years","rooms_per_100m2"]:
#         if col in df.columns: df[col] = winsorize(df[col])

#     price_feats = ["price_tnd","Area","room","bathroom","pieces",
#                    "distance_to_capital","amenity_score","age_years","latt","long","state"]
#     price_imp = IterativeImputer(estimator=BayesianRidge(), max_iter=10, random_state=42, verbose=0)
#     block = df[price_feats].copy()
#     imputed = pd.DataFrame(price_imp.fit_transform(block), columns=price_feats, index=df.index)
#     df["price_tnd"] = winsorize(imputed["price_tnd"])

#     knn_geo = KNNImputer(n_neighbors=5)
#     df[["latt","long","distance_to_capital"]] = knn_geo.fit_transform(df[["latt","long","distance_to_capital"]])
#     knn_struct = KNNImputer(n_neighbors=5)
#     df[["Area","pieces","room","bathroom"]] = knn_struct.fit_transform(df[["Area","pieces","room","bathroom"]])

#     df["age_years"]       = df["age_years"].fillna(df["age_years"].median())
#     df["state"]           = df["state"].fillna(df["state"].mode()[0])
#     df["rooms_per_100m2"] = np.where(df["Area"]>0,(df["room"]/df["Area"])*100, df["rooms_per_100m2"].median())
#     df["rooms_per_100m2"] = winsorize(df["rooms_per_100m2"])

#     city_mode = df.groupby("governorate")["city"].agg(lambda x: x.mode()[0] if x.notna().any() else "Unknown")
#     df["city"] = df.apply(lambda r: city_mode.get(r["governorate"],"Unknown") if pd.isna(r["city"]) else r["city"], axis=1)
#     loc_mode  = df.groupby("city")["location"].agg(lambda x: x.mode()[0] if x.notna().any() else "Unknown")
#     df["location"] = df.apply(lambda r: loc_mode.get(r["city"],"Unknown") if pd.isna(r["location"]) else r["location"], axis=1)

#     le_gov = LabelEncoder()
#     df["governorate_enc"] = le_gov.fit_transform(df["governorate"])
#     city_freq = df["city"].value_counts() / len(df)
#     df["city_freq"] = df["city"].map(city_freq)
#     loc_freq  = df["location"].value_counts() / len(df)
#     df["location_freq"] = df["location"].map(loc_freq)
#     df["log_price"] = np.log1p(df["price_tnd"])

#     features = ["Area","pieces","room","bathroom","age_years","state",
#                 "latt","long","distance_to_capital",
#                 "garage","garden","concierge","beach_view","mountain_view",
#                 "pool","elevator","furnished","equipped_kitchen","central_heating","air_conditioning",
#                 "amenity_score","rooms_per_100m2","governorate_enc","city_freq","location_freq"]

#     X = df[features].copy()
#     y = df["log_price"].copy()
#     for col in X.columns:
#         if X[col].isnull().any(): X[col] = X[col].fillna(X[col].median())

#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     mdl = HistGradientBoostingRegressor(max_iter=500, max_depth=6, learning_rate=0.05, random_state=42)
#     mdl.fit(X_train, y_train)

#     y_pred = np.expm1(mdl.predict(X_test))
#     y_true = np.expm1(y_test.values)
#     return mdl, le_gov, city_freq, loc_freq, features, r2_score(y_true,y_pred), mean_absolute_error(y_true,y_pred), len(df)


# def run_predict(mdl, le_gov, city_freq, loc_freq, features, inp):
#     gov     = inp["governorate"].strip()
#     amenity = sum([inp[k] for k in ["garage","garden","concierge","beach_view","mountain_view",
#                                      "pool","elevator","furnished","equipped_kitchen",
#                                      "central_heating","air_conditioning"]])
#     r_ratio = (inp["room"] / inp["area"] * 100) if inp["area"] > 0 else 0
#     gov_enc = int(le_gov.transform([gov])[0]) if gov in le_gov.classes_ else 0
#     city_f  = float(city_freq.get(inp["city"],  city_freq.median()))
#     loc_f   = float(loc_freq.get(inp["location"], loc_freq.median()))
#     sample  = pd.DataFrame([[
#         inp["area"], inp["pieces"], inp["room"], inp["bathroom"],
#         inp["age_years"], inp["state"], inp["latt"], inp["long"], inp["distance"],
#         inp["garage"], inp["garden"], inp["concierge"], inp["beach_view"], inp["mountain_view"],
#         inp["pool"], inp["elevator"], inp["furnished"], inp["equipped_kitchen"],
#         inp["central_heating"], inp["air_conditioning"],
#         amenity, r_ratio, gov_enc, city_f, loc_f,
#     ]], columns=features)
#     return float(np.expm1(mdl.predict(sample)[0]))


# # ─────────────────────────────────────────────────────────────────
# # LOAD MODEL
# # ─────────────────────────────────────────────────────────────────
# with st.spinner("Initialising Aqari AI engine…"):
#     model, le_gov, city_freq, loc_freq, features, r2_val, mae_val, n_samples = load_and_train()

# # ─────────────────────────────────────────────────────────────────
# # HEADER
# # ─────────────────────────────────────────────────────────────────
# st.markdown("""
# <div style="padding:1.5rem 0 1rem; border-bottom:1px solid #1e293b; margin-bottom:2rem;">
#   <div style="display:flex; align-items:baseline; gap:1rem;">
#     <span style="font-family:'Cormorant Garamond',serif; font-size:2.8rem; font-weight:700;
#                  background:linear-gradient(135deg,#8a6a20,#c9a84c,#e8c96a);
#                  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
#                  background-clip:text; line-height:1;">Aqari</span>
#     <span style="font-family:'DM Sans',sans-serif; font-size:0.9rem; color:#4a5a72;
#                  letter-spacing:0.22em; text-transform:uppercase;">
#       Tunisia Property Estimator
#     </span>
#   </div>
#   <p style="font-size:0.88rem; color:#7a8da8; margin-top:0.3rem; margin-bottom:0;">
#     AI-powered valuations &nbsp;·&nbsp; Trained on real Tunisian transaction data &nbsp;·&nbsp; Instant estimates
#   </p>
# </div>
# """, unsafe_allow_html=True)

# # ─────────────────────────────────────────────────────────────────
# # TWO-COLUMN LAYOUT
# # ─────────────────────────────────────────────────────────────────
# col_left, col_right = st.columns([1, 1.15], gap="large")

# # ══════════════════════════════════════════════
# # LEFT — Input Form
# # ══════════════════════════════════════════════
# with col_left:
    
#     st.markdown('<div class="panel-title">🏗️ Property Details</div>', unsafe_allow_html=True)

#     # Location
#     st.markdown('<div class="section-label">📍 Location</div>', unsafe_allow_html=True)
#     gov_options = sorted(CITIES_BY_GOV.keys())
#     governorate = st.selectbox("Governorate", options=gov_options,
#                                index=gov_options.index("tunis"), key="gov")
#     city_options = CITIES_BY_GOV.get(governorate, [governorate])
#     city = st.selectbox("City / Delegation", options=city_options, key="city_sel")

#     latt_def, long_def, dist_def = GOV_COORDS.get(governorate, (36.82, 10.17, 20.0))
 
#     st.markdown("---")

#     # Specs
#     st.markdown('<div class="section-label">📐 Surface & Rooms</div>', unsafe_allow_html=True)
#     area = st.slider("Area (m²)", min_value=30, max_value=2000, value=200, step=10)
#     sc1, sc2, sc3, sc4 = st.columns(4)
#     with sc1: pieces    = st.number_input("Pieces",    min_value=1, max_value=50,  value=6)
#     with sc2: room      = st.number_input("Rooms",     min_value=1, max_value=40,  value=3)
#     with sc3: bathroom  = st.number_input("Bathrooms", min_value=1, max_value=20,  value=2)
#     with sc4: age_years = st.number_input("Age (yrs)", min_value=0, max_value=120, value=5)

#     st.markdown('<div class="section-label">🏛️ Condition</div>', unsafe_allow_html=True)
#     state_sel = st.selectbox(
#         "Building Condition",
#         options=[(0,"Under Construction"),(1,"Good / Move-in Ready"),(2,"Needs Renovation")],
#         format_func=lambda x: x[1], index=1,
#     )
#     state_val = state_sel[0]

#     st.markdown("---")

#     # Amenities
#     st.markdown('<div class="section-label">✨ Amenities</div>', unsafe_allow_html=True)
#     ac1, ac2, ac3 = st.columns(3)
#     with ac1:
#         garage    = st.checkbox("🚗 Garage",    value=True)
#         garden    = st.checkbox("🌿 Garden",    value=False)
#         pool      = st.checkbox("🏊 Pool",      value=False)
#         elevator  = st.checkbox("🛗 Elevator",  value=False)
#     with ac2:
#         furnished        = st.checkbox("🛋️ Furnished",  value=False)
#         concierge        = st.checkbox("👤 Concierge",   value=False)
#         equipped_kitchen = st.checkbox("🍳 Kitchen",     value=True)
#     with ac3:
#         central_heating  = st.checkbox("🔥 Heating",     value=True)
#         air_conditioning = st.checkbox("❄️ A/C",         value=True)
#         beach_view       = st.checkbox("🌊 Beach View",  value=False)
#         mountain_view    = st.checkbox("⛰️ Mountain",    value=False)

#     st.markdown("<br>", unsafe_allow_html=True)
#     predict_btn = st.button("✦  Estimate Property Value")
#     st.markdown('</div>', unsafe_allow_html=True)

# # ══════════════════════════════════════════════
# # RIGHT — Results
# # ══════════════════════════════════════════════
# with col_right:
#     inputs = dict(
#         area=float(area), pieces=float(pieces), room=float(room),
#         bathroom=float(bathroom), age_years=float(age_years),
#         state=float(state_val), latt=latt_def, long=long_def, distance=dist_def,
#         governorate=governorate, city=city, location=city,
#         garage=int(garage), garden=int(garden), concierge=int(concierge),
#         beach_view=int(beach_view), mountain_view=int(mountain_view),
#         pool=int(pool), elevator=int(elevator), furnished=int(furnished),
#         equipped_kitchen=int(equipped_kitchen), central_heating=int(central_heating),
#         air_conditioning=int(air_conditioning),
#     )
    
#     if "last_price" not in st.session_state:
#         st.session_state.last_price = None

#     if predict_btn:
#         with st.spinner(""):
#             time.sleep(0.3)
#         st.session_state.last_price  = run_predict(model, le_gov, city_freq, loc_freq, features, inputs)
#         st.session_state.last_inputs = inputs.copy()

#     if st.session_state.last_price is not None:
#         price_tnd = st.session_state.last_price
#         price_eur = price_tnd * 0.31
#         price_usd = price_tnd * 0.32
#         price_m2  = price_tnd / area if area > 0 else 0
#         low_15    = price_tnd * 0.85
#         high_15   = price_tnd * 1.15
#         low_25    = price_tnd * 0.75
#         high_25   = price_tnd * 1.25
#         amenity_cnt = sum([inputs[k] for k in ["garage","garden","concierge","beach_view","mountain_view",
#                                                 "pool","elevator","furnished","equipped_kitchen",
#                                                 "central_heating","air_conditioning"]])
#         cond_map = {0:"Under Construction", 1:"Move-in Ready", 2:"Needs Renovation"}

#         # Big result card
#         st.markdown(f"""
#         <div class="result-card">
#           <div style="font-size:0.72rem; color:#7a8da8; letter-spacing:0.22em;
#                       text-transform:uppercase; margin-bottom:0.8rem; font-family:'DM Sans',sans-serif;">
#             Estimated Market Value
#           </div>
#           <div class="price-display">{price_tnd:,.0f}
#             <span style="font-size:2.2rem; opacity:0.7;">TND</span>
#           </div>
#           <div class="price-sub">≈ {price_eur:,.0f} EUR &nbsp;·&nbsp; ≈ {price_usd:,.0f} USD</div>
#           <div style="margin-top:1.1rem; display:flex; justify-content:center; flex-wrap:wrap; gap:0.3rem;">
#             <span class="badge badge-gold">🏙️ {governorate}</span>
#             <span class="badge badge-teal">📐 {area} m²</span>
#             <span class="badge badge-gold">{price_m2:,.0f} TND/m²</span>
#             <span class="badge badge-teal">🛏 {room:.0f} rooms</span>
#             <span class="badge badge-green">✓ {amenity_cnt}/11 amenities</span>
#           </div>
#           <div style="margin-top:1rem; font-size:0.72rem; color:#4a5a72; font-family:'DM Mono',monospace;">
#             ±15% confidence band &nbsp;—&nbsp;
#             <span style="color:#c9a84c">{low_15:,.0f}</span> to
#             <span style="color:#c9a84c">{high_15:,.0f} TND</span>
#           </div>
#         </div>
#         """, unsafe_allow_html=True)

#         # 3 detail panels
#         p1, p2, p3 = st.columns(3)

#         with p1:
#             st.markdown("""<div style="font-family:'Cormorant Garamond',serif; font-size:0.9rem;
#                 color:#c9a84c; letter-spacing:0.1em; text-transform:uppercase;
#                 border-bottom:1px solid #1e293b; padding-bottom:0.45rem; margin-bottom:0.7rem;">
#                 💰 Price Ranges</div>""", unsafe_allow_html=True)
#             st.markdown(f"""<div>
#               <div class="info-row"><span class="info-label">Optimistic +25%</span>
#                 <span class="info-value" style="color:#4ade80">{high_25:,.0f}</span></div>
#               <div class="info-row"><span class="info-label">High +15%</span>
#                 <span class="info-value" style="color:#86efac">{high_15:,.0f}</span></div>
#               <div class="info-row"><span class="info-label">AI Estimate</span>
#                 <span class="info-value" style="color:#c9a84c;font-weight:700">{price_tnd:,.0f}</span></div>
#               <div class="info-row"><span class="info-label">Conservative −15%</span>
#                 <span class="info-value" style="color:#fca5a5">{low_15:,.0f}</span></div>
#               <div class="info-row"><span class="info-label">Pessimistic −25%</span>
#                 <span class="info-value" style="color:#f87171">{low_25:,.0f}</span></div>
#               <div class="info-row"><span class="info-label">Per m²</span>
#                 <span class="info-value">{price_m2:,.0f} TND</span></div>
#             </div>""", unsafe_allow_html=True)

#         with p2:
#             st.markdown("""<div style="font-family:'Cormorant Garamond',serif; font-size:0.9rem;
#                 color:#c9a84c; letter-spacing:0.1em; text-transform:uppercase;
#                 border-bottom:1px solid #1e293b; padding-bottom:0.45rem; margin-bottom:0.7rem;">
#                 🏗️ Summary</div>""", unsafe_allow_html=True)
#             st.markdown(f"""<div>
#               <div class="info-row"><span class="info-label">Governorate</span><span class="info-value">{governorate}</span></div>
#               <div class="info-row"><span class="info-label">City</span><span class="info-value">{city}</span></div>
#               <div class="info-row"><span class="info-label">Area</span><span class="info-value">{area} m²</span></div>
#               <div class="info-row"><span class="info-label">Rooms / Baths</span><span class="info-value">{room:.0f} / {bathroom:.0f}</span></div>
#               <div class="info-row"><span class="info-label">Pieces</span><span class="info-value">{pieces:.0f}</span></div>
#               <div class="info-row"><span class="info-label">Age</span><span class="info-value">{age_years:.0f} yrs</span></div>
#               <div class="info-row"><span class="info-label">Condition</span><span class="info-value">{cond_map.get(state_val,'—')}</span></div>
#             </div>""", unsafe_allow_html=True)

#         with p3:
#             st.markdown("""<div style="font-family:'Cormorant Garamond',serif; font-size:0.9rem;
#                 color:#c9a84c; letter-spacing:0.1em; text-transform:uppercase;
#                 border-bottom:1px solid #1e293b; padding-bottom:0.45rem; margin-bottom:0.7rem;">
#                 ✨ Amenities</div>""", unsafe_allow_html=True)
#             amenities = [
#                 ("🚗 Garage",garage),("🌿 Garden",garden),("🏊 Pool",pool),
#                 ("🛗 Elevator",elevator),("🛋️ Furnished",furnished),("👤 Concierge",concierge),
#                 ("🍳 Kitchen",equipped_kitchen),("🔥 Heating",central_heating),
#                 ("❄️ A/C",air_conditioning),("🌊 Beach View",beach_view),("⛰️ Mountain",mountain_view),
#             ]
#             items = "".join([
#                 f'<div class="amenity-item {"active" if v else ""}">{"✓" if v else "○"} {lbl}</div>'
#                 for lbl, v in amenities
#             ])
#             st.markdown(f'<div class="amenity-grid">{items}</div>', unsafe_allow_html=True)

#         # Currency strip
#         st.markdown("<br>", unsafe_allow_html=True)
#         m1, m2, m3, m4 = st.columns(4)
#         m1.metric("TND",          f"{price_tnd:,.0f}")
#         m2.metric("EUR (≈×0.31)", f"{price_eur:,.0f}")
#         m3.metric("USD (≈×0.32)", f"{price_usd:,.0f}")
#         m4.metric("Price / m²",   f"{price_m2:,.0f} TND")

#     else:
#         st.markdown("""
#         <div class="placeholder-box">
#           <div style="font-size:3.5rem; margin-bottom:1rem; opacity:0.12;">🏡</div>
#           <div style="font-family:'Cormorant Garamond',serif; font-size:1.5rem;
#                       color:#4a5a72; margin-bottom:0.5rem;">
#             Your estimate will appear here
#           </div>
#           <div style="font-size:0.85rem; color:#2d4a6a;">
#             Fill in the property details on the left, then click<br>
#             <strong style="color:#c9a84c;">✦ Estimate Property Value</strong>
#           </div>
#         </div>
#         """, unsafe_allow_html=True)

# # ─────────────────────────────────────────────────────────────────
# # FOOTER
# # ─────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="watermark">
#   Aqari · Tunisia Property Estimator &nbsp;·&nbsp;
#   AI model trained on Tunisian real estate data &nbsp;·&nbsp;
#   Estimates are indicative only
# </div>
# """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import numpy as np
import warnings
import time
import joblib
import json

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Aqari · Tunisia Property Estimator",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

:root {
    --bg:        #080c14;
    --surface:   #0e1421;
    --card:      #111827;
    --card2:     #0d1520;
    --border:    #1e293b;
    --gold:      #c9a84c;
    --gold-lt:   #e8c96a;
    --gold-dk:   #8a6a20;
    --teal:      #0ea5c9;
    --teal-lt:   #38c0e0;
    --green:     #4ade80;
    --text:      #e8edf5;
    --text-muted:#7a8da8;
    --text-dim:  #4a5a72;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: var(--text);
    background-color: var(--bg);
}
.stApp { background: var(--bg); }
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stSidebar"] { display: none; }
.block-container { padding: 2rem 2.5rem 3rem !important; max-width: 1500px; }

[data-testid="stNumberInput"] input,
.stTextInput input {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.88rem !important;
    padding: 0.5rem 0.75rem !important;
}
[data-testid="stNumberInput"] input:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 2px rgba(201,168,76,0.15) !important;
}

[data-testid="stSelectbox"] > div > div {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.88rem !important;
}
[data-testid="stSelectbox"] > div > div:hover { border-color: var(--gold-dk) !important; }

[data-testid="stSlider"] > div > div > div > div {
    background: linear-gradient(90deg, var(--gold-dk), var(--gold)) !important;
}
[data-testid="stSlider"] > div > div > div > div > div {
    background: var(--gold) !important;
    border: 2px solid var(--gold-lt) !important;
    box-shadow: 0 0 10px rgba(201,168,76,0.5) !important;
}

[data-testid="stCheckbox"] > label > div:first-child {
    background: var(--card) !important;
    border-color: var(--border) !important;
    border-radius: 4px !important;
}
[data-testid="stCheckbox"] > label > div[aria-checked="true"] {
    background: var(--gold) !important;
    border-color: var(--gold) !important;
}
[data-testid="stCheckbox"] label p { color: var(--text-muted) !important; font-size: 0.83rem !important; }

.stButton > button {
    background: linear-gradient(135deg, var(--gold-dk), var(--gold), var(--gold-lt)) !important;
    color: #060a10 !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    letter-spacing: 0.06em !important;
    padding: 0.75rem 2rem !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 20px rgba(201,168,76,0.35) !important;
    width: 100% !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(201,168,76,0.55) !important;
}

hr { border-color: var(--border) !important; margin: 1.2rem 0 !important; }
label { color: var(--text-muted) !important; font-size: 0.82rem !important; }
.stMarkdown p { color: var(--text-muted) !important; font-size: 0.85rem; }

[data-testid="stMetric"] {
    background: var(--card2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 0.9rem 1.1rem;
}
[data-testid="stMetric"] label { color: var(--text-muted) !important; font-size: 0.75rem !important; }
[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: var(--gold) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.6rem !important;
    font-weight: 600 !important;
}

[data-testid="stExpander"] {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
}
[data-testid="stExpander"] summary p { color: var(--text-muted) !important; font-size: 0.82rem !important; }

.panel {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.6rem 1.8rem;
}
.panel-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.15rem;
    font-weight: 600;
    color: var(--gold);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding-bottom: 0.7rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.2rem;
}
.section-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--text-dim);
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin: 1.2rem 0 0.5rem;
}
.result-card {
    background: linear-gradient(135deg, #0c1525 0%, #111e32 100%);
    border: 1px solid var(--gold-dk);
    border-radius: 16px;
    padding: 2.2rem 2rem;
    text-align: center;
    box-shadow: 0 0 50px rgba(201,168,76,0.07), inset 0 0 80px rgba(201,168,76,0.025);
    margin-bottom: 1.5rem;
}
.price-display {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.8rem;
    font-weight: 700;
    background: linear-gradient(135deg, var(--gold-dk), var(--gold), var(--gold-lt));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.05;
    letter-spacing: -0.02em;
}
.price-sub {
    font-family: 'DM Mono', monospace;
    font-size: 1.05rem;
    color: var(--text-muted);
    margin-top: 0.4rem;
}
.badge {
    display: inline-block;
    padding: 0.22rem 0.75rem;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 500;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin: 0.25rem 0.2rem;
}
.badge-gold  { background: rgba(201,168,76,0.12); color: var(--gold);    border: 1px solid rgba(201,168,76,0.28); }
.badge-teal  { background: rgba(14,165,201,0.10); color: var(--teal-lt); border: 1px solid rgba(14,165,201,0.22); }
.badge-green { background: rgba(74,222,128,0.10); color: var(--green);   border: 1px solid rgba(74,222,128,0.22); }
.info-row {
    display: flex; justify-content: space-between; align-items: center;
    padding: 0.55rem 0; border-bottom: 1px solid var(--border); font-size: 0.83rem;
}
.info-row:last-child { border-bottom: none; }
.info-label { color: var(--text-muted); }
.info-value { color: var(--text); font-family: 'DM Mono', monospace; font-weight: 500; }
.amenity-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.4rem; margin-top: 0.5rem; }
.amenity-item {
    display: flex; align-items: center; gap: 0.45rem;
    font-size: 0.79rem; color: var(--text-muted);
    padding: 0.35rem 0.55rem;
    background: var(--surface); border-radius: 6px; border: 1px solid var(--border);
}
.amenity-item.active { color: var(--gold); border-color: rgba(201,168,76,0.28); background: rgba(201,168,76,0.04); }
.placeholder-box {
    text-align: center; padding: 5rem 2rem;
    border: 1px dashed var(--border); border-radius: 16px; background: var(--card2);
}
.watermark {
    font-family: 'Cormorant Garamond', serif; font-size: 0.72rem; color: var(--text-dim);
    text-align: center; letter-spacing: 0.15em; text-transform: uppercase;
    margin-top: 2.5rem; padding-top: 1rem; border-top: 1px solid var(--border);
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────────
CITIES_BY_GOV = {
    "Ariana":       ["Ariana Ville","Ettadhamen","Kalaat Landalous","La Soukra","Mnihla","Raoued","Sidi Thabet"],
    "Ben Arous":    ["Ben Arous","Boumhel Bassatine","El Mourouj","Ezzahra","Fouchana","Hammam Chatt","Hammam Lif","Mohamadia","Mornag","Mégrine","Nouvelle Medina","Rades"],
    "Bizerte":      ["Bizerte Nord","Bizerte Sud","Metline"],
    "Béja":         ["Béja"],
    "Djerba":       ["Ajim","Djerba","Houmt Souk","Midoun"],
    "El Kasserine": ["El Kasserine"],
    "Gabès":        ["Gabès Ville"],
    "Gafsa":        ["Gafsa"],
    "Jendouba":     ["Tabarka"],
    "Kairouan":     ["Kairouan Ville"],
    "Kébili":       ["Douz"],
    "La Manouba":   ["Borj El Amri","Douar Hicher","El Battan","Jedaida","La Manouba","Mornaguia","Oued Ellil","Tebourba"],
    "Le Kef":       ["Le Kef"],
    "Mahdia":       ["Mahdia Ville"],
    "Medenine":     ["Medenine"],
    "Monastir":     ["Monastir Ville"],
    "Nabeul":       ["Beni Khiar","Hammamet","Nabeul"],
    "Sfax":         ["Menzel Chaker","Sakiet Eddaier","Sakiet Ezzit","Sfax Ouest","Sfax Sud","Sfax Ville"],
    "Siliana":      ["Siliana"],
    "Sousse":       ["Akouda","Hammam Sousse","Sousse Jaouhara","Sousse Riadh","Sousse Ville"],
    "Tataouine":    ["Tataouine"],
    "Zaghouan":     ["Zaghouan"],
    "tunis":        ["Carthage","Cité El Khadra","El Hrairia","El Kabaria","El Menzah","El Omrane","El Omrane Superieur","El Ouardia","Ettahrir","La Goulette","La Marsa","Le Bardo","Le Kram","Sidi Hassine","Tunis"],
}
GOV_COORDS = {
    "tunis":(36.82,10.17,2.0), "Ariana":(36.87,10.19,8.0),
    "Ben Arous":(36.65,10.22,15.0), "La Manouba":(36.81,10.10,7.0),
    "Nabeul":(36.45,10.73,65.0), "Sousse":(35.83,10.64,115.0),
    "Monastir":(35.77,10.82,135.0), "Mahdia":(35.50,11.07,170.0),
    "Sfax":(34.74,10.76,270.0), "Kairouan":(35.67,10.10,155.0),
    "Bizerte":(37.27,9.87,60.0), "Béja":(36.73,9.18,90.0),
    "Jendouba":(36.50,8.78,145.0), "Le Kef":(36.18,8.71,180.0),
    "Siliana":(36.08,9.37,140.0), "Zaghouan":(36.40,10.14,55.0),
    "Djerba":(33.87,10.85,330.0), "Gabès":(33.88,9.54,310.0),
    "Medenine":(33.35,10.50,380.0), "Tataouine":(32.93,10.45,450.0),
    "Kébili":(33.71,8.97,370.0), "Gafsa":(34.43,8.78,270.0),
    "El Kasserine":(35.17,8.83,230.0),
}

# ─────────────────────────────────────────────────────────────────
# MODEL — Load from saved files (no retraining)
# ─────────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def load_model():
    """
    Load the pre-trained model and all artifacts saved from the notebook.
    Expected files in the same directory as this script:
        aqari_model.pkl
        aqari_le_gov.pkl
        aqari_city_freq.json
        aqari_loc_freq.json
        aqari_features.json
        aqari_meta.json
    """
    mdl    = joblib.load("aqari_model.pkl")
    le_gov = joblib.load("aqari_le_gov.pkl")

    with open("aqari_city_freq.json") as f:
        city_freq = pd.Series(json.load(f))

    with open("aqari_loc_freq.json") as f:
        loc_freq = pd.Series(json.load(f))

    with open("aqari_features.json") as f:
        features = json.load(f)

    with open("aqari_meta.json") as f:
        meta = json.load(f)

    return mdl, le_gov, city_freq, loc_freq, features, meta


def run_predict(mdl, le_gov, city_freq, loc_freq, features, meta, inp):
    gov = inp["governorate"].strip()

    # Feature engineering (same as training)
    amenity = sum([
        inp[k] for k in [
            "garage","garden","concierge","beach_view","mountain_view",
            "pool","elevator","furnished","equipped_kitchen",
            "central_heating","air_conditioning"
        ]
    ])

    r_ratio = (inp["room"] / inp["area"] * 100) if inp["area"] > 0 else 0

    # Encoding (same as training)
    gov_enc = int(le_gov.transform([gov])[0]) if gov in le_gov.classes_ else 0
    city_f  = float(city_freq.get(inp["city"], meta["city_freq_median"]))
    loc_f   = float(loc_freq.get(inp["location"], meta["loc_freq_median"]))

    # ✅ EXACT SAME STRUCTURE AS JUPYTER
    sample_dict = {
        "area": inp["area"],
        "pieces": inp["pieces"],
        "room": inp["room"],
        "bathroom": inp["bathroom"],
        "age_years": inp["age_years"],
        "state": inp["state"],

        "garage": inp["garage"],
        "garden": inp["garden"],
        "concierge": inp["concierge"],
        "beach_view": inp["beach_view"],
        "mountain_view": inp["mountain_view"],
        "pool": inp["pool"],
        "elevator": inp["elevator"],
        "furnished": inp["furnished"],
        "equipped_kitchen": inp["equipped_kitchen"],
        "central_heating": inp["central_heating"],
        "air_conditioning": inp["air_conditioning"],

        "amenity_score": amenity,
        "rooms_per_100m2": r_ratio,
        "governorate_enc": gov_enc,
        "city_freq": city_f,
        "location_freq": loc_f,
    }

    # ✅ SAFE alignment (this was missing)
    sample = pd.DataFrame([sample_dict]).reindex(columns=features, fill_value=0)

    return float(np.expm1(mdl.predict(sample)[0]))

# ─────────────────────────────────────────────────────────────────
# LOAD MODEL
# ─────────────────────────────────────────────────────────────────
with st.spinner("Initialising Aqari AI engine…"):
    try:
        model, le_gov, city_freq, loc_freq, features, meta = load_model()
        model_loaded = True
    except FileNotFoundError as e:
        model_loaded = False
        missing_file = str(e)

if not model_loaded:
    st.error(f"""
    ⚠️ **Model files not found.**

    Please run the notebook cell that saves the model first, then place these files
    in the same directory as `HousePredictor.py`:

    - `aqari_model.pkl`
    - `aqari_le_gov.pkl`
    - `aqari_city_freq.json`
    - `aqari_loc_freq.json`
    - `aqari_features.json`
    - `aqari_meta.json`

    Missing: `{missing_file}`
    """)
    st.stop()

# ─────────────────────────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding:1.5rem 0 1rem; border-bottom:1px solid #1e293b; margin-bottom:2rem;">
  <div style="display:flex; align-items:baseline; gap:1rem;">
    <span style="font-family:'Cormorant Garamond',serif; font-size:2.8rem; font-weight:700;
                 background:linear-gradient(135deg,#8a6a20,#c9a84c,#e8c96a);
                 -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                 background-clip:text; line-height:1;">Aqari</span>
    <span style="font-family:'DM Sans',sans-serif; font-size:0.9rem; color:#4a5a72;
                 letter-spacing:0.22em; text-transform:uppercase;">
      Tunisia Property Estimator
    </span>
  </div>
  <p style="font-size:0.88rem; color:#7a8da8; margin-top:0.3rem; margin-bottom:0;">
    AI-powered valuations &nbsp;·&nbsp; Trained on real Tunisian transaction data &nbsp;·&nbsp; Instant estimates
  </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# TWO-COLUMN LAYOUT
# ─────────────────────────────────────────────────────────────────
col_left, col_right = st.columns([1, 1.15], gap="large")

# ══════════════════════════════════════════════
# LEFT — Input Form
# ══════════════════════════════════════════════
with col_left:

    st.markdown('<div class="panel-title">🏗️ Property Details</div>', unsafe_allow_html=True)

    # Location
    st.markdown('<div class="section-label">📍 Location</div>', unsafe_allow_html=True)
    gov_options = sorted(CITIES_BY_GOV.keys())
    governorate = st.selectbox("Governorate", options=gov_options,
                               index=gov_options.index("tunis"), key="gov")
    city_options = CITIES_BY_GOV.get(governorate, [governorate])
    city = st.selectbox("City / Delegation", options=city_options, key="city_sel")

    latt_def, long_def, dist_def = GOV_COORDS.get(governorate, (36.82, 10.17, 20.0))

    st.markdown("---")

    # Specs
    st.markdown('<div class="section-label">📐 Surface & Rooms</div>', unsafe_allow_html=True)
    area = st.slider("Area (m²)", min_value=30, max_value=2000, value=200, step=10)
    sc1, sc2, sc3, sc4 = st.columns(4)
    with sc1: pieces    = st.number_input("Pieces",    min_value=1, max_value=50,  value=6)
    with sc2: room      = st.number_input("Rooms",     min_value=1, max_value=40,  value=3)
    with sc3: bathroom  = st.number_input("Bathrooms", min_value=1, max_value=20,  value=2)
    with sc4: age_years = st.number_input("Age (yrs)", min_value=0, max_value=120, value=5)

    st.markdown('<div class="section-label">🏛️ Condition</div>', unsafe_allow_html=True)
    state_sel = st.selectbox(
        "Building Condition",
        options=[(1,"Under Construction"),(0,"Good / Move-in Ready"),(2,"Needs Renovation")],
        format_func=lambda x: x[1], index=1,
    )
    state_val = state_sel[0]

    st.markdown("---")

    # Amenities
    st.markdown('<div class="section-label">✨ Amenities</div>', unsafe_allow_html=True)
    ac1, ac2, ac3 = st.columns(3)
    with ac1:
        garage    = st.checkbox("🚗 Garage",    value=True)
        garden    = st.checkbox("🌿 Garden",    value=False)
        pool      = st.checkbox("🏊 Pool",      value=False)
        elevator  = st.checkbox("🛗 Elevator",  value=False)
    with ac2:
        furnished        = st.checkbox("🛋️ Furnished",  value=False)
        concierge        = st.checkbox("👤 Concierge",   value=False)
        equipped_kitchen = st.checkbox("🍳 Kitchen",     value=True)
    with ac3:
        central_heating  = st.checkbox("🔥 Heating",     value=True)
        air_conditioning = st.checkbox("❄️ A/C",         value=True)
        beach_view       = st.checkbox("🌊 Beach View",  value=False)
        mountain_view    = st.checkbox("⛰️ Mountain",    value=False)

    st.markdown("<br>", unsafe_allow_html=True)
    predict_btn = st.button("✦  Estimate Property Value")
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════
# RIGHT — Results
# ══════════════════════════════════════════════
with col_right:
    inputs = dict(
        area=float(area), pieces=float(pieces), room=float(room),
        bathroom=float(bathroom), age_years=float(age_years),
        state=float(state_val), latt=latt_def, long=long_def, distance=dist_def,
        governorate=governorate, city=city, location=city,
        garage=int(garage), garden=int(garden), concierge=int(concierge),
        beach_view=int(beach_view), mountain_view=int(mountain_view),
        pool=int(pool), elevator=int(elevator), furnished=int(furnished),
        equipped_kitchen=int(equipped_kitchen), central_heating=int(central_heating),
        air_conditioning=int(air_conditioning),
    )

    if "last_price" not in st.session_state:
        st.session_state.last_price = None

    if predict_btn:
        with st.spinner(""):
            time.sleep(0.3)
        st.session_state.last_price  = run_predict(model, le_gov, city_freq, loc_freq, features, meta, inputs)
        st.session_state.last_inputs = inputs.copy()

    if st.session_state.last_price is not None:
        price_tnd = st.session_state.last_price
        price_eur = price_tnd * 0.31
        price_usd = price_tnd * 0.32
        price_m2  = price_tnd / area if area > 0 else 0
        low_15    = price_tnd * 0.85
        high_15   = price_tnd * 1.15
        low_25    = price_tnd * 0.75
        high_25   = price_tnd * 1.25
        amenity_cnt = sum([inputs[k] for k in ["garage","garden","concierge","beach_view","mountain_view",
                                                "pool","elevator","furnished","equipped_kitchen",
                                                "central_heating","air_conditioning"]])
        cond_map = {0:"Under Construction", 1:"Move-in Ready", 2:"Needs Renovation"}

        # Big result card
        st.markdown(f"""
        <div class="result-card">
          <div style="font-size:0.72rem; color:#7a8da8; letter-spacing:0.22em;
                      text-transform:uppercase; margin-bottom:0.8rem; font-family:'DM Sans',sans-serif;">
            Estimated Market Value
          </div>
          <div class="price-display">{price_tnd:,.0f}
            <span style="font-size:2.2rem; opacity:0.7;">TND</span>
          </div>
          <div class="price-sub">≈ {price_eur:,.0f} EUR &nbsp;·&nbsp; ≈ {price_usd:,.0f} USD</div>
          <div style="margin-top:1.1rem; display:flex; justify-content:center; flex-wrap:wrap; gap:0.3rem;">
            <span class="badge badge-gold">🏙️ {governorate}</span>
            <span class="badge badge-teal">📐 {area} m²</span>
            <span class="badge badge-gold">{price_m2:,.0f} TND/m²</span>
            <span class="badge badge-teal">🛏 {room:.0f} rooms</span>
            <span class="badge badge-green">✓ {amenity_cnt}/11 amenities</span>
          </div>
          <div style="margin-top:1rem; font-size:0.72rem; color:#4a5a72; font-family:'DM Mono',monospace;">
            ±15% confidence band &nbsp;—&nbsp;
            <span style="color:#c9a84c">{low_15:,.0f}</span> to
            <span style="color:#c9a84c">{high_15:,.0f} TND</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # 3 detail panels
        p1, p2, p3 = st.columns(3)

        with p1:
            st.markdown("""<div style="font-family:'Cormorant Garamond',serif; font-size:0.9rem;
                color:#c9a84c; letter-spacing:0.1em; text-transform:uppercase;
                border-bottom:1px solid #1e293b; padding-bottom:0.45rem; margin-bottom:0.7rem;">
                💰 Price Ranges</div>""", unsafe_allow_html=True)
            st.markdown(f"""<div>
              <div class="info-row"><span class="info-label">Optimistic +25%</span>
                <span class="info-value" style="color:#4ade80">{high_25:,.0f}</span></div>
              <div class="info-row"><span class="info-label">High +15%</span>
                <span class="info-value" style="color:#86efac">{high_15:,.0f}</span></div>
              <div class="info-row"><span class="info-label">AI Estimate</span>
                <span class="info-value" style="color:#c9a84c;font-weight:700">{price_tnd:,.0f}</span></div>
              <div class="info-row"><span class="info-label">Conservative −15%</span>
                <span class="info-value" style="color:#fca5a5">{low_15:,.0f}</span></div>
              <div class="info-row"><span class="info-label">Pessimistic −25%</span>
                <span class="info-value" style="color:#f87171">{low_25:,.0f}</span></div>
              <div class="info-row"><span class="info-label">Per m²</span>
                <span class="info-value">{price_m2:,.0f} TND</span></div>
            </div>""", unsafe_allow_html=True)

        with p2:
            st.markdown("""<div style="font-family:'Cormorant Garamond',serif; font-size:0.9rem;
                color:#c9a84c; letter-spacing:0.1em; text-transform:uppercase;
                border-bottom:1px solid #1e293b; padding-bottom:0.45rem; margin-bottom:0.7rem;">
                🏗️ Summary</div>""", unsafe_allow_html=True)
            st.markdown(f"""<div>
              <div class="info-row"><span class="info-label">Governorate</span><span class="info-value">{governorate}</span></div>
              <div class="info-row"><span class="info-label">City</span><span class="info-value">{city}</span></div>
              <div class="info-row"><span class="info-label">Area</span><span class="info-value">{area} m²</span></div>
              <div class="info-row"><span class="info-label">Rooms / Baths</span><span class="info-value">{room:.0f} / {bathroom:.0f}</span></div>
              <div class="info-row"><span class="info-label">Pieces</span><span class="info-value">{pieces:.0f}</span></div>
              <div class="info-row"><span class="info-label">Age</span><span class="info-value">{age_years:.0f} yrs</span></div>
              <div class="info-row"><span class="info-label">Condition</span><span class="info-value">{cond_map.get(state_val,'—')}</span></div>
            </div>""", unsafe_allow_html=True)

        with p3:
            st.markdown("""<div style="font-family:'Cormorant Garamond',serif; font-size:0.9rem;
                color:#c9a84c; letter-spacing:0.1em; text-transform:uppercase;
                border-bottom:1px solid #1e293b; padding-bottom:0.45rem; margin-bottom:0.7rem;">
                ✨ Amenities</div>""", unsafe_allow_html=True)
            amenities = [
                ("🚗 Garage",garage),("🌿 Garden",garden),("🏊 Pool",pool),
                ("🛗 Elevator",elevator),("🛋️ Furnished",furnished),("👤 Concierge",concierge),
                ("🍳 Kitchen",equipped_kitchen),("🔥 Heating",central_heating),
                ("❄️ A/C",air_conditioning),("🌊 Beach View",beach_view),("⛰️ Mountain",mountain_view),
            ]
            items = "".join([
                f'<div class="amenity-item {"active" if v else ""}">{"✓" if v else "○"} {lbl}</div>'
                for lbl, v in amenities
            ])
            st.markdown(f'<div class="amenity-grid">{items}</div>', unsafe_allow_html=True)

        # Currency strip
        st.markdown("<br>", unsafe_allow_html=True)
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("TND",          f"{price_tnd:,.0f}")
        m2.metric("EUR (≈×0.31)", f"{price_eur:,.0f}")
        m3.metric("USD (≈×0.32)", f"{price_usd:,.0f}")
        m4.metric("Price / m²",   f"{price_m2:,.0f} TND")

    else:
        st.markdown("""
        <div class="placeholder-box">
          <div style="font-size:3.5rem; margin-bottom:1rem; opacity:0.12;">🏡</div>
          <div style="font-family:'Cormorant Garamond',serif; font-size:1.5rem;
                      color:#4a5a72; margin-bottom:0.5rem;">
            Your estimate will appear here
          </div>
          <div style="font-size:0.85rem; color:#2d4a6a;">
            Fill in the property details on the left, then click<br>
            <strong style="color:#c9a84c;">✦ Estimate Property Value</strong>
          </div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="watermark">
  Aqari · Tunisia Property Estimator &nbsp;·&nbsp;
  AI model trained on Tunisian real estate data &nbsp;·&nbsp;
  Estimates are indicative only
</div>
""", unsafe_allow_html=True)
