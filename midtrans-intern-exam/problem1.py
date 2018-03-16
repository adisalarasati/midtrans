from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

address = ["PERUM. PURI ARSANA JL. RAYA CIPUTAT PARUNG KM.11 E-12 IDN",
          "Jalan budi mulia gang F3 No.29D Rt.04 Rw.02, Jakarta Selatan. Indonesia.",
          "Level 1, Tower 6, Avenue 3, The Horizon, Bangsar South, No. 4, Jalan Kerinchi",
          "Jalan budi mulia Gg. F2 Nomor 29 D RT. 04 Rw.02, JakSel",
          "Green garden M17A no.44 Jakarta Barat - 11520",
          "Jln budi mulia Gg. F2 Nomor 28 D RT. 04 Rw.02, JakSel. IDN.",
          "Jl BudiMulia Gang f2 Nomor 28D RT. 04/02, Jakarta Selatan. IDN."
          ]
vec = TfidfVectorizer()
X = vec.fit_transform(address)

S = cosine_similarity(X)

print('Similarity of the texts:\n', S)
