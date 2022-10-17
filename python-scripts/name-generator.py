MISSION = "MINUSCA"
SITES = ["BAMBARI",
         "BANGASSOU",
         "BANGUI",
         "BANGUI_HQ",
         "BERBERATI",
         "BIRAO",
         "BOSSANGOA",
         "BOUAR",
         "BRIA",
         "BANGUI_DR",
         "KAGA",
         "KAGABANDORO",
         "NDELE",
         "OBO",
         "PAOUA",
         "SIBUT"]

CONNECTION = ["DMVPN", "DBAS"]

dashboard_base = f"PEMO - WAN Visualization Tool - 1_MISSION - {MISSION}\n"

f = open("naming.txt", "w")
f.write(dashboard_base)
visualization_base = f"PEMO - WAN Visualization Tool - TSVB - Site Bar - {MISSION}\n"
f.write(visualization_base)

for site in SITES:
    value = f"PEMO - WAN Visualization Tool - 2_SITE - {MISSION}_{site}\n"
    value = f"PEMO - WAN Visualization Tool - TSVB - CONNECTION BAR -  {MISSION}_{site}\n"
    f.write(value)
    for con in CONNECTION:
        value = f"PEMO - WAN Visualization Tool - 3_CONNECTION - {MISSION}_{site}_{con}\n"
        f.write(value)
        value = f"PEMO - WAN Visualization Tool - TSVB - {MISSION}_{site}_{con}_INTERFACE"
        f.write(value)
