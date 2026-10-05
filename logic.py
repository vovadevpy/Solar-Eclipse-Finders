import math
from datetime import datetime, timezone

#[RU] - Для русской локали перевод
#[EN] - For EN locale translate
#---------------------------------------


# [ru] # положение солнца и луны
# [en] # sun and moon positions
# [ru] # определение параметров солнечного затмения
# [en] # solar eclipse parameters
# [ru] # поиск ближайшего полного солнечного затмения
# [en] # nearest total solar eclipse


# [ru] # основные астрономические константы
# [en] # main astronomical constants



DEG = math.pi / 180.0                    # коэффициент перевода градусов в радианы
J2000 = 2451545.0                         # стандартная эпоха j2000
DAYS_PER_JULIAN_CENTURY = 36525.0       # количество дней в юлианском веке
SYNODIC_MONTH_DAYS = 29.530588861       # длительность синодического месяца

AU_KM = 149597870.7                      # длина астрономической единицы в километрах
SUN_RADIUS_KM = 696000.0                 # радиус солнца в километрах
MOON_RADIUS_KM = 1737.4                  # радиус луны в километрах
EARTH_RADIUS_KM = 6371.0                 # радиус земли в километрах
EARTH_ORBIT_ECCENTRICITY = 0.016708634   # эксцентриситет орбиты земли (конкретно данная констарнта максимально приближена к реальной)
#рассинхронизация является штатной ситуацией
MOON_MEAN_DISTANCE_KM = 385000.56        # среднее расстояние от земли до луны

# [ru] # коэффициенты расчёта положения луны
# [en] # coefficients for calculating the moon's position

MOON_D = [0, 2, 2, 0, 0, 0, 2, 2, 2, 2, 0, 1, 0, 2, 0, 0, 4, 0, 4, 2, 2, 1, 1, 2, 2, 4, 2, 0, 2, 2, 1, 2, 0, 0, 2, 2, 2, 4, 0, 3, 2, 4, 0, 2, 2, 2, 4, 0, 4, 1, 2, 0, 1, 3, 4, 2, 0, 1, 2, 2]
MOON_M = [0, 0, 0, 0, 1, 0, 0, -1, 0, -1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, -1, 0, 0, 0, 1, 0, -1, 0, -2, 1, 2, -2, 0, 0, -1, 0, 0, 1, -1, 2, 2, 1, -1, 0, 0, -1, 0, 1, 0, 1, 0, 0, -1, 2, 1, 0, 0]
MOON_MP = [1, -1, 0, 2, 0, 0, -2, -1, 1, 0, -1, 0, 1, 0, 1, 1, -1, 3, -2, -1, 0, -1, 0, 1, 2, 0, -3, -2, -1, -2, 1, 0, 2, 0, -1, 1, 0, -1, 2, -1, 1, -2, -1, -1, -2, 0, 1, 4, 0, -2, 0, 2, 1, -2, -3, 2, 1, -1, 3, -1]
MOON_F = [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, -2, 2, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, -2, 2, 0, 2, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0, -2, -2, 0, 0, 0, 0, 0, 0, 0, -2]
MOON_LR_L = [6288774, 1274027, 658314, 213618, -185116, -114332, 58793, 57066, 53322, 45758, -40923, -34720, -30383, 15327, -12528, 10980, 10675, 10034, 8548, -7888, -6766, -5163, 4987, 4036, 3994, 3861, 3665, -2689, -2602, 2390, -2348, 2236, -2120, -2069, 2048, -1773, -1595, 1215, -1110, -892, -810, 759, -713, -700, 691, 596, 549, 537, 520, -487, -399, -381, 351, -340, 330, 327, -323, 299, 294, 0]
MOON_LR_R = [-20905355, -3699111, -2955968, -569925, 48888, -3149, 246158, -152138, -170733, -204586, -129620, 108743, 104755, 10321, 0, 79661, -34782, -23210, -21636, 24208, 30824, -8379, -16675, -12831, -10445, -11650, 14403, -7003, 0, 10056, 6322, -9884, 5751, 0, -4950, 4130, 0, -3958, 0, 3258, 2616, -1897, -2117, 2354, 0, 0, -1423, -1117, -1571, -1739, 0, -4421, 0, 0, 0, 0, 1165, 0, 0, 8752]
MOON_B_D = [0, 0, 0, 2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 4, 0, 0, 0, 1, 0, 0, 0, 1, 0, 4, 4, 0, 4, 2, 2, 2, 2, 0, 2, 2, 2, 2, 4, 2, 2, 0, 2, 1, 1, 0, 2, 1, 2, 0, 4, 4, 1, 4, 1, 4, 2]
MOON_B_M = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, -1, -1, -1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 1, 0, -1, -2, 0, 1, 1, 1, 1, 1, 0, -1, 1, 0, -1, 0, 0, 0, -1, -2]
MOON_B_MP = [0, 1, 1, 0, -1, -1, 0, 2, 1, 2, 0, -2, 1, 0, -1, 0, -1, -1, -1, 0, 0, -1, 0, 1, 1, 0, 0, 3, 0, -1, 1, -2, 0, 2, 1, -2, 3, 2, -3, -1, 0, 0, 1, 0, 1, 1, 0, 0, -2, -1, 1, -2, 2, -2, -1, 1, 1, -1, 0, 0]
MOON_B_F = [1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 3, 1, 1, 1, -1, -1, -1, 1, -1, 1, -3, 1, -3, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, 3, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1]
MOON_B_L = [5128122, 280602, 277693, 173237, 55413, 46271, 32573, 17198, 9266, 8822, 8216, 4324, 4200, -3359, 2463, 2211, 2065, -1870, 1828, -1794, -1749, -1565, -1491, -1475, -1410, -1344, -1335, 1107, 1021, 833, 777, 671, 607, 596, 491, -451, 439, 422, 421, -366, -351, 331, 315, 302, -283, -229, 223, 223, -220, -220, -185, 181, -177, 176, 166, -164, 132, -119, 115, 107]


# [ru] # переводит unix-время в юлианскую дату
# [en] # converts unix time to julian date
def julian_date(ms: float) -> float:
    return ms / 86400000.0 + 2440587.5


# [ru] # рассчитывает поправку delta t
# [en] # calculates the delta t correction
def get_delta_t(jd: float) -> float:
    year = 2000 + (jd - J2000) / 365.2425
    if year < 2005:
        t = year - 2000
        return 63.86 + 0.3345*t - 0.060374*t*t + 0.0017275*t**3 + 0.000651814*t**4 + 0.00002373599*t**5
    if year < 2050:
        t = year - 2000
        return 62.92 + 0.32217*t + 0.005589*t*t
    u = (year - 1820) / 100
    if year < 2150:
        return -20 + 32*u*u - 0.5628*(2150-year)
    return 32*u*u - 20


# [ru] # переводит время в шкалу tt
# [en] # converts time to the tt time scale
def julian_date_tt(ms: float) -> float:
    return julian_date(ms) + get_delta_t(julian_date(ms)) / 86400.0


# [ru] # нормализует угол до 0–360°
# [en] # normalizes an angle to 0–360°
def normalize_deg(deg: float) -> float:
    return ((deg % 360.0) + 360.0) % 360.0


# [ru] # нормализует угол в радианах
# [en] # normalizes an angle in radians
def normalize_rad(rad: float) -> float:
    return rad % (2.0 * math.pi)


# [ru] # рассчитывает расстояние земли до солнца
# [en] # calculates the earth-sun distance
def earth_radius_km(ms: float) -> float:
    jd_tt = julian_date_tt(ms)
    T = (jd_tt - J2000) / 36525.0
    M = (357.52911 + 35999.05029*T - 0.0001537*T*T) * DEG
    return 1 - EARTH_ORBIT_ECCENTRICITY * math.cos(M)


# [ru] # рассчитывает звёздное время гринвича
# [en] # calculates greenwich sidereal time
def greenwich_sidereal_rad(ms: float) -> float:
    jd = julian_date(ms)
    T = (jd - J2000) / 36525.0
    gmst = 280.46061837 + 360.98564736629*(jd - J2000) + 0.000387933*T*T - (T*T*T)/38710000.0
    return normalize_rad(gmst * DEG)


# [ru] # рассчитывает наклон эклиптики
# [en] # calculates the obliquity of the ecliptic
def mean_obliquity_rad(T: float) -> float:
    return (23.439291 - 0.0130042*T - 0.00000016*T*T + 0.000000504*T*T*T) * DEG


# [ru] # переводит земные координаты в экваториальные
# [en] # converts earth-fixed coordinates to equatorial coordinates
def earth_fixed_to_equatorial(v, gmst):
    c, s = math.cos(gmst), math.sin(gmst)
    return (v[0]*c - v[1]*s, v[0]*s + v[1]*c, v[2])


# [ru] # переводит экваториальные координаты в эклиптические
# [en] # converts equatorial coordinates to ecliptic coordinates
def equatorial_to_ecliptic(v, obliq):
    c, s = math.cos(obliq), math.sin(obliq)
    return (v[0], v[1]*c + v[2]*s, -v[1]*s + v[2]*c)


# [ru] # переводит сферические координаты в декартовы
# [en] # converts spherical coordinates to cartesian coordinates
def spherical_to_cartesian(lon, lat, r):
    cl = math.cos(lat)
    return (r*cl*math.cos(lon), r*cl*math.sin(lon), r*math.sin(lat))


# [ru] # вычитает два вектора
# [en] # subtracts two vectors
def vec_sub(a, b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])


# [ru] # рассчитывает скалярное произведение
# [en] # calculates the dot product
def vec_dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]


# [ru] # рассчитывает длину вектора
# [en] # calculates vector length
def vec_len(a):
    return math.sqrt(vec_dot(a, a))


# [ru] # масштабирует вектор
# [en] # scales a vector
def vec_scale(a, s):
    return (a[0]*s, a[1]*s, a[2]*s)


# [ru] # рассчитывает положение наблюдателя на земле
# [en] # calculates the observer's position on earth
def observer_ecliptic_vector_km(ms, lat_deg, lon_deg):
    T = (julian_date_tt(ms) - J2000) / 36525.0
    gmst = greenwich_sidereal_rad(ms)
    obliq = mean_obliquity_rad(T)
    ef = spherical_to_cartesian(lon_deg*DEG, lat_deg*DEG, EARTH_RADIUS_KM)
    eq = earth_fixed_to_equatorial(ef, gmst)
    return equatorial_to_ecliptic(eq, obliq)


# [ru] # рассчитывает положение солнца
# [en] # calculates the sun's position
def sun_ecliptic_vector_km(ms):
    jd_tt = julian_date_tt(ms)
    T = (jd_tt - J2000) / 36525.0
    L0 = normalize_deg(280.46646 + 36000.76983*T + 0.0003032*T*T)
    M = (357.52911 + 35999.05029*T - 0.0001537*T*T) * DEG
    C = ((1.914602 - 0.004817*T - 0.000014*T*T)*math.sin(M)
         + (0.019993 - 0.000101*T)*math.sin(2*M)
         + 0.000289*math.sin(3*M)) * DEG
    sun_lon = normalize_rad(L0*DEG + C)
    dist_au = earth_radius_km(ms)
    return spherical_to_cartesian(sun_lon, 0.0, dist_au * AU_KM)


# [ru] # рассчитывает положение луны
# [en] # calculates the moon's position
def moon_ecliptic_position(ms):
    jd_tt = julian_date_tt(ms)
    T = (jd_tt - J2000) / 36525.0
    T2, T3, T4 = T*T, T*T*T, T*T*T*T

    Lp = normalize_deg(218.3164477 + 481267.88123421*T - 0.0015786*T2 + T3/538841.0 - T4/65194000.0)
    D = normalize_deg(297.8501921 + 445267.1114034*T - 0.0018819*T2 + T3/545868.0 - T4/113065000.0)
    M = normalize_deg(357.5291092 + 35999.0502909*T - 0.0001536*T2 + T3/24490000.0)
    Mp = normalize_deg(134.9633964 + 477198.8675055*T + 0.0087414*T2 + T3/69699.0 - T4/14712000.0)
    F = normalize_deg(93.2720950 + 483202.0175233*T - 0.0036539*T2 - T3/3526000.0 + T4/863310000.0)

    A1 = 119.75 + 131.849*T
    A2 = 53.09 + 479264.290*T
    A3 = 313.45 + 481266.484*T
    E = 1 - 0.002516*T - 0.0000074*T2
    E2 = E*E

    sigma_l = 0.0
    sigma_r = 0.0
    sigma_b = 0.0

    for i in range(60):
        e_pow = E if abs(MOON_M[i]) == 1 else (E2 if abs(MOON_M[i]) == 2 else 1.0)
        arg = (MOON_D[i]*D + MOON_M[i]*M + MOON_MP[i]*Mp + MOON_F[i]*F) * DEG
        sigma_l += MOON_LR_L[i] * e_pow * math.sin(arg)
        sigma_r += MOON_LR_R[i] * e_pow * math.cos(arg)

        b_pow = E if abs(MOON_B_M[i]) == 1 else (E2 if abs(MOON_B_M[i]) == 2 else 1.0)
        b_arg = (MOON_B_D[i]*D + MOON_B_M[i]*M + MOON_B_MP[i]*Mp + MOON_B_F[i]*F) * DEG
        sigma_b += MOON_B_L[i] * b_pow * math.sin(b_arg)

    sigma_l += 3958*math.sin(A1*DEG) + 1962*math.sin((Lp-F)*DEG) + 318*math.sin(A2*DEG)
    sigma_b += (-2235*math.sin(Lp*DEG) + 382*math.sin(A3*DEG)
                + 175*math.sin((A1-F)*DEG) + 175*math.sin((A1+F)*DEG)
                + 127*math.sin((Lp-Mp)*DEG) - 115*math.sin((Lp+Mp)*DEG))

    return {
        "lon": normalize_rad((Lp + sigma_l/1_000_000.0)*DEG),
        "lat": (sigma_b/1_000_000.0)*DEG,
        "distance": MOON_MEAN_DISTANCE_KM + sigma_r/1000.0,
    }


# [ru] # переводит положение луны в вектор
# [en] # converts the moon's position to a vector
def moon_ecliptic_vector_km(ms):
    moon = moon_ecliptic_position(ms)
    return spherical_to_cartesian(moon["lon"], moon["lat"], moon["distance"])


# [ru] # рассчитывает площадь перекрытия двух кругов
# [en] # calculates the overlap area of two circles
def circle_overlap_area(R, r, d):
    if d >= R + r:
        return 0.0
    if d <= abs(R-r):
        m = min(R, r)
        return math.pi*m*m
    p1 = R*R*math.acos(max(-1, min(1, (d*d + R*R - r*r)/(2*d*R))))
    p2 = r*r*math.acos(max(-1, min(1, (d*d + r*r - R*R)/(2*d*r))))
    p3 = 0.5*math.sqrt(max(0, (-d+r+R)*(d+r-R)*(d-r+R)*(d+r+R)))
    return p1 + p2 - p3


# [ru] # определяет параметры солнечного затмения
# [en] # determines solar eclipse parameters
def solar_eclipse_at(ms, lat_deg, lon_deg):
    obs = observer_ecliptic_vector_km(ms, lat_deg, lon_deg)
    sun = sun_ecliptic_vector_km(ms)
    moon = moon_ecliptic_vector_km(ms)

    to_sun = vec_sub(sun, obs)
    to_moon = vec_sub(moon, obs)
    d_sun = vec_len(to_sun)
    d_moon = vec_len(to_moon)

    sun_ang = math.asin(min(1.0, SUN_RADIUS_KM / d_sun))
    moon_ang = math.asin(min(1.0, MOON_RADIUS_KM / d_moon))

    cos_sep = vec_dot(to_sun, to_moon) / (d_sun*d_moon)
    separation = math.acos(max(-1.0, min(1.0, cos_sep)))

    up = vec_scale(obs, 1.0 / max(1e-12, vec_len(obs)))
    sun_alt = math.asin(max(-1.0, min(1.0, vec_dot(to_sun, up) / d_sun)))

    is_eclipse = separation < sun_ang + moon_ang
    eclipse_type = "none"
    if is_eclipse:
        diff = abs(moon_ang - sun_ang)
        if separation < diff:
            eclipse_type = "total" if moon_ang >= sun_ang else "annular"
        else:
            eclipse_type = "partial"

    magnitude = max(0.0, (sun_ang + moon_ang - separation) / (2*sun_ang))
    overlap = circle_overlap_area(sun_ang, moon_ang, separation) if is_eclipse else 0.0
    obscured = min(1.0, overlap / (math.pi*sun_ang*sun_ang))

    return {
        "visible": is_eclipse and sun_alt > 0,
        "type": eclipse_type,
        "magnitude": magnitude,
        "obscured": obscured,
        "separation_deg": separation / DEG,
        "sun_alt_deg": sun_alt / DEG,
    }


# [ru] # рассчитывает дату среднего новолуния
# [en] # calculates the date of mean new moon
def mean_new_moon_jde(k):
    T = k / 1236.85
    return (2451550.09766 + SYNODIC_MONTH_DAYS*k
            + 0.00015437*T*T
            - 0.000000150*T*T*T
            + 0.00000000073*T*T*T*T)


# [ru] # переводит jde в миллисекунды
# [en] # converts jde to milliseconds
def jde_to_ms(jde):
    return (jde - 2440587.5) * 86400000.0


# [ru] # уточняет момент минимального сближения луны и солнца
# [en] # refines the moment of minimum moon-sun separation
def refine_local_minimum(lo_ms, hi_ms, lat_deg, lon_deg):
    phi = (math.sqrt(5) - 1) / 2
    a, b = lo_ms, hi_ms
    c = b - phi*(b-a)
    d = a + phi*(b-a)
    fc = solar_eclipse_at(c, lat_deg, lon_deg)["separation_deg"]
    fd = solar_eclipse_at(d, lat_deg, lon_deg)["separation_deg"]

    for _ in range(80):
        if (b-a) <= 0.01:
            break
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - phi*(b-a)
            fc = solar_eclipse_at(c, lat_deg, lon_deg)["separation_deg"]
        else:
            a, c, fc = c, d, fd
            d = a + phi*(b-a)
            fd = solar_eclipse_at(d, lat_deg, lon_deg)["separation_deg"]

    ms = (a+b)*0.5
    return ms, solar_eclipse_at(ms, lat_deg, lon_deg)


# [ru] # ищет минимальное сближение луны и солнца в диапазоне
# [en] # finds the minimum moon-sun separation in a time range
def find_local_eclipse_minimum(scan_start, scan_end, lat_deg, lon_deg):
    step_ms = 5*60*1000
    best_t = scan_start
    best_sep = float("inf")
    t = scan_start
    while t <= scan_end:
        data = solar_eclipse_at(t, lat_deg, lon_deg)
        if data["separation_deg"] < best_sep:
            best_sep = data["separation_deg"]
            best_t = t
        t += step_ms

    data = solar_eclipse_at(scan_end, lat_deg, lon_deg)
    if data["separation_deg"] < best_sep:
        best_t = scan_end

    lo = max(scan_start, best_t-step_ms)
    hi = min(scan_end, best_t+step_ms)
    return refine_local_minimum(lo, hi, lat_deg, lon_deg)


# [ru] # ищет ближайшее полное солнечное затмение
# [en] # finds the nearest total solar eclipse
def find_next_total_solar_eclipse(start_ms, lat_deg, lon_deg, max_years=3000, progress=None):
    lat_deg = max(-90.0, min(90.0, lat_deg))
    lon_deg = ((lon_deg + 180) % 360) - 180
    end_ms = start_ms + max_years*365.25*86400000.0

    t0 = (julian_date(start_ms) - 2451550.09766) / SYNODIC_MONTH_DAYS
    k = math.floor(t0) - 2

    count = 0
    while True:
        jde = mean_new_moon_jde(k)
        new_moon_ms = jde_to_ms(jde)
        if new_moon_ms > end_ms:
            return None

        if new_moon_ms >= start_ms - 20*3600*1000:
            moon = moon_ecliptic_position(new_moon_ms)
            moon_lat_deg = abs(moon["lat"] / DEG)
            if moon_lat_deg < 2.0:
                scan_start = max(start_ms, new_moon_ms - 20*3600*1000)
                scan_end = min(end_ms, new_moon_ms + 20*3600*1000)
                if scan_end > scan_start:
                    eclipse_ms, data = find_local_eclipse_minimum(
                        scan_start,
                        scan_end,
                        lat_deg,
                        lon_deg
                    )
                    if eclipse_ms >= start_ms and data["visible"] and data["type"] == "total":
                        return eclipse_ms, data

        k += 1
        count += 1
        if progress and count % 4 == 0:
            progress(max(0.0, (new_moon_ms-start_ms)/(365.25*86400000.0)))


# [ru] # форматирует дату в utc и местное солнечное время
# [en] # formats the date in utc and local solar time
def format_dates(ms, lon_deg):
    utc_dt = datetime.fromtimestamp(ms/1000.0, tz=timezone.utc)
    local_ms = ms + (lon_deg/15.0)*3600*1000
    local_solar_dt = datetime.fromtimestamp(local_ms/1000.0, tz=timezone.utc)

    return (
        utc_dt.strftime("%d.%m.%Y %H:%M UTC"),
        local_solar_dt.strftime("%d.%m.%Y %H:%M")
    )