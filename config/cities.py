india_cities = [
    "Delhi", "Mumbai", "Bangalore", "Chennai", "Hyderabad", "Kolkata",
    "Pune", "Ahmedabad", "Jaipur", "Chandigarh", "Noida", "Gurgaon",
    "Faridabad", "Ghaziabad", "Lucknow", "Kanpur", "Indore", "Bhopal",
    "Nagpur", "Surat", "Vadodara", "Rajkot", "Udaipur",
    "Kochi", "Trivandrum", "Thrissur", "Coimbatore", "Madurai",
    "Trichy", "Salem", "Erode",
    "Vijayawada", "Visakhapatnam", "Guntur",
    "Warangal", "Nizamabad",
    "Patna", "Gaya", "Muzaffarpur",
    "Ranchi", "Jamshedpur", "Dhanbad",
    "Bhubaneswar", "Cuttack", "Rourkela",
    "Guwahati", "Silchar",
    "Shillong", "Imphal", "Aizawl",
    "Agra", "Mathura", "Meerut", "Aligarh",
    "Dehradun", "Haridwar", "Rishikesh",
    "Shimla", "Manali", "Dharamshala",
    "Jammu", "Srinagar", "Leh"
]

international_cities = [
    # UK & Europe
    "London", "Manchester", "Birmingham", "Edinburgh",
    "Paris", "Lyon", "Marseille",
    "Berlin", "Munich", "Frankfurt",
    "Amsterdam", "Rotterdam",
    "Madrid", "Barcelona",
    "Rome", "Milan",
    "Zurich", "Geneva",

    # USA & Canada
    "New York", "Los Angeles", "San Francisco", "Seattle",
    "Chicago", "Boston", "Austin", "Dallas",
    "Toronto", "Vancouver", "Montreal",

    # Middle East
    "Dubai", "Abu Dhabi", "Doha", "Riyadh", "Jeddah",

    # Asia-Pacific
    "Singapore", "Kuala Lumpur", "Bangkok",
    "Jakarta", "Manila",
    "Tokyo", "Osaka", "Kyoto",
    "Seoul", "Busan",
    "Hong Kong",
    "Shanghai", "Beijing", "Shenzhen",
    "Sydney", "Melbourne", "Brisbane",
    "Auckland"
]

more_india_cities = [
    # Uttar Pradesh
    "Varanasi", "Prayagraj", "Ayodhya", "Bareilly", "Moradabad",
    "Saharanpur", "Muzaffarnagar", "Jhansi", "Etawah",

    # Maharashtra
    "Nashik", "Aurangabad", "Kolhapur", "Solapur", "Amravati",
    "Akola", "Latur", "Satara",

    # Karnataka
    "Mysore", "Mangalore", "Udupi", "Hubli", "Belgaum", "Bellary",

    # Tamil Nadu
    "Tirunelveli", "Thoothukudi", "Vellore", "Kanchipuram",
    "Thanjavur", "Dindigul",

    # Andhra Pradesh
    "Nellore", "Kadapa", "Kurnool", "Anantapur", "Ongole",

    # Telangana
    "Karimnagar", "Khammam", "Mahbubnagar", "Adilabad",

    # West Bengal
    "Asansol", "Durgapur", "Siliguri", "Howrah",

    # Rajasthan
    "Jodhpur", "Bikaner", "Ajmer", "Alwar", "Bharatpur",

    # Gujarat
    "Bhavnagar", "Jamnagar", "Porbandar", "Junagadh",

    # Madhya Pradesh
    "Gwalior", "Jabalpur", "Ujjain", "Sagar", "Rewa",

    # Punjab & Haryana
    "Ludhiana", "Jalandhar", "Patiala", "Bathinda",
    "Panipat", "Sonipat", "Rohtak",

    # Bihar
    "Darbhanga", "Bhagalpur", "Purnia",

    # Jharkhand
    "Bokaro", "Hazaribagh",

    # Chhattisgarh
    "Raipur", "Bilaspur", "Durg",

    # Uttarakhand
    "Haldwani", "Rudrapur"
]

more_international_cities = [
    # Europe (expanded)
    "Vienna", "Prague", "Budapest", "Warsaw", "Krakow",
    "Stockholm", "Oslo", "Helsinki", "Copenhagen",
    "Brussels", "Antwerp",
    "Lisbon", "Porto",
    "Athens", "Thessaloniki",

    # USA (expanded)
    "Denver", "Phoenix", "Las Vegas", "San Diego",
    "San Jose", "Oakland", "Palo Alto",
    "Miami", "Orlando", "Tampa",
    "Atlanta", "Charlotte", "Raleigh",
    "Washington", "Baltimore",
    "Detroit", "Cleveland",
    "Minneapolis", "St. Paul",

    # South America
    "Sao Paulo", "Rio de Janeiro", "Buenos Aires",
    "Santiago", "Lima", "Bogota", "Medellin",

    # Africa
    "Cairo", "Alexandria",
    "Nairobi", "Mombasa",
    "Lagos", "Abuja",
    "Accra",
    "Cape Town", "Johannesburg", "Durban",

    # Middle East (expanded)
    "Muscat", "Salalah",
    "Manama", "Kuwait City",
    "Amman", "Beirut",

    # Asia (expanded)
    "Hanoi", "Ho Chi Minh City",
    "Phnom Penh", "Vientiane",
    "Taipei", "Kaohsiung",
    "Karachi", "Lahore", "Islamabad",
    "Dhaka", "Chittagong",
    "Colombo", "Kandy",
    "Kathmandu", "Pokhara",

    # Oceania
    "Perth", "Adelaide", "Canberra",
    "Wellington", "Christchurch"
]

ALL_CITIES = (
    india_cities
    + more_india_cities
    + international_cities
    + more_international_cities
)