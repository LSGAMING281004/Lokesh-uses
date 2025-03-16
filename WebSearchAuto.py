import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Set up Edge WebDriver in default mode (no user profile)
edge_options = webdriver.EdgeOptions()
#edge_options.add_argument("--inprivate")  # Open Edge in incognito mode (optional)

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)

# List of unique search terms
search_terms = [
    # 🔹 General BCA & Study Topics
    "Best programming languages for BCA students", 
    "How to become a software developer",
    "Important subjects in BCA course",
    "Best project ideas for BCA final year",
    "Top IT certifications for students",
    "How to improve coding skills as a student",
    "Latest technology trends in 2025",
    
    # 🔹 Software Development & App Development
    "How to build a mobile app from scratch",
    "Best programming languages for app development",
    "Top frameworks for mobile app development",
    "Why choose Flutter for mobile development",
    "Best databases for mobile apps",
    "How to integrate Firebase with Flutter",
    "Best software development practices in 2025",
    "What is Agile methodology in software development",
    
    # 🔹 Flutter & Android Development
    "Best resources to learn Flutter",
    "Top Flutter UI libraries",
    "How to deploy a Flutter app",
    "How to use Riverpod in Flutter",
    "Flutter vs React Native: Which is better?",
    "How to optimize performance in Flutter apps",
    "Best state management solutions in Flutter",
    
    # 🔹 Tamil & Localized Topics
    "Best Tamil YouTube channels to learn programming",
    "Tamil programming tutorials for beginners",
    "How to get IT jobs in Tamil Nadu",
    "Top software companies in Chennai",
    "Tamil coding communities and groups",
    "How to contribute to open-source projects in Tamil",
    
    # 🔹 Career & Job Opportunities
    "Best job opportunities for BCA graduates",
    "How to build a strong resume for software jobs",
    "How to prepare for software developer interviews",
    "Best websites to apply for IT jobs in India",
    "Freelancing opportunities for software developers",
    
    # 🔹 Tech Trends & News
    "Top software development trends in 2025",
    "Best AI tools for developers",
    "How AI is changing software development",
    "What is blockchain technology?",
    "Latest updates in mobile app development",
    "Future of programming languages in 2030"
]


# Perform searches without repeating words
for i in range(min(30, len(search_terms))):  # Ensures max 30 searches, no repeats
    driver.get("https://www.bing.com")
    search_box = driver.find_element("name", "q")
    
    query = random.choice(search_terms)  # Pick a random word from the list
    search_terms.remove(query)  # Remove the used word to prevent repetition
    
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    
    print(f"Search {i+1}: {query}")
    
    time.sleep(random.randint(5, 10))  # Wait randomly to avoid bot detection

driver.quit()  # Close the browser after searches
