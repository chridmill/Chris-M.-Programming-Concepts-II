"""
ChrisMiller_Population_CM.py
Florida Population Database & Growth Simulator
Uses SQLite database: population_CM.db
"""

import sqlite3
import random
import matplotlib.pyplot as plt


def create_and_populate_2025() -> None:
    """
    Create the SQLite database 'population_CM.db' and the 'population' table.
    Insert 2025 population data for 10 Florida cities.
    Uses INSERT OR IGNORE to safely run multiple times.
    """
    conn = sqlite3.connect('population_CM.db')
    cursor = conn.cursor()

    # Create table with composite primary key to prevent duplicate (city, year) rows
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER,
            PRIMARY KEY (city, year)
        )
    ''')

    # 2025 starting populations (realistic estimates based on recent data)
    initial_data = [
        ("Jacksonville", 2025, 1000000),
        ("Miami", 2025, 460000),
        ("Tampa", 2025, 410000),
        ("Orlando", 2025, 330000),
        ("St. Petersburg", 2025, 265000),
        ("Tallahassee", 2025, 195000),
        ("Fort Lauderdale", 2025, 190000),
        ("Gainesville", 2025, 145000),
        ("Sarasota", 2025, 140000),
        ("Boca Raton", 2025, 100000),
    ]

    for city, year, pop in initial_data:
        cursor.execute('''
            INSERT OR IGNORE INTO population (city, year, population)
            VALUES (?, ?, ?)
        ''', (city, year, pop))

    conn.commit()
    print("✅ Database 'population_CM.db' created and 2025 data inserted.")
    conn.close()


def simulate_population_growth() -> None:
    """
    Simulate population growth/decline for 2026–2045 (20 years).
    Applies a random annual rate between -2% and +6% for each city/year.
    Only inserts data if it doesn't already exist (safe to rerun).
    """
    conn = sqlite3.connect('population_CM.db')
    cursor = conn.cursor()

    # Get all cities that have 2025 data
    cursor.execute("SELECT DISTINCT city FROM population WHERE year = 2025")
    cities = [row[0] for row in cursor.fetchall()]

    for city in cities:
        # Get the most recent population (start from 2025 or last simulated year)
        cursor.execute("""
            SELECT population FROM population 
            WHERE city = ? 
            ORDER BY year DESC 
            LIMIT 1
        """, (city,))
        current_pop = cursor.fetchone()[0]

        for year in range(2026, 2046):  # 2026 to 2045 inclusive
            # Skip if this year already exists for the city
            cursor.execute("SELECT COUNT(*) FROM population WHERE city = ? AND year = ?", (city, year))
            if cursor.fetchone()[0] > 0:
                continue

            # Random growth/decline rate (-2% to +6%)
            rate = random.uniform(-0.02, 0.06)
            new_pop = int(current_pop * (1 + rate))
            if new_pop < 0:
                new_pop = 0

            cursor.execute('''
                INSERT OR IGNORE INTO population (city, year, population)
                VALUES (?, ?, ?)
            ''', (city, year, new_pop))

            current_pop = new_pop  # carry forward for next year

    conn.commit()
    print("✅ Population growth/decline simulation (2026–2045) completed.")
    conn.close()


def get_cities() -> list[str]:
    """
    Return a sorted list of all cities in the database.
    """
    conn = sqlite3.connect('population_CM.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT city FROM population ORDER BY city")
    cities = [row[0] for row in cursor.fetchall()]
    conn.close()
    return cities


def plot_population_growth(city_name: str) -> None:
    """
    Query the database for a specific city's population over all years
    and display a line graph using matplotlib.
    """
    conn = sqlite3.connect('population_CM.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT year, population 
        FROM population 
        WHERE city = ? 
        ORDER BY year
    """, (city_name,))
    data = cursor.fetchall()
    conn.close()

    if not data:
        print(f"❌ No data found for {city_name}.")
        return

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    plt.figure(figsize=(11, 6))
    plt.plot(years, populations, marker='o', linestyle='-', color='blue', linewidth=2, markersize=5)
    plt.title(f"Population Growth/Decline: {city_name} (2025–2045)", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Population", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Smart y-axis formatting
    max_pop = max(populations)
    if max_pop >= 1_000_000:
        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x/1_000_000:.1f}M'))
    elif max_pop >= 10_000:
        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x/1_000)}K'))

    plt.xticks(years, rotation=45)
    plt.tight_layout()
    plt.show()


def main() -> None:
    """
    Main program: sets up the database, runs the simulation,
    lists the 10 Florida cities, lets the user choose one, and displays the graph.
    """
    print("=== Florida Population Database & Simulator (population_CM.db) ===\n")

    create_and_populate_2025()
    simulate_population_growth()

    print("\n10 Florida Cities Available:")
    cities = get_cities()
    for i, city in enumerate(cities, 1):
        print(f"  {i:2}. {city}")

    while True:
        try:
            choice = int(input("\nEnter the number of the city to visualize (1-10): "))
            if 1 <= choice <= len(cities):
                selected = cities[choice - 1]
                print(f"\n📊 Generating population graph for {selected}...")
                plot_population_growth(selected)
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\n✅ Program complete! Close the plot window when done.")


if __name__ == "__main__":
    # Optional: set seed for consistent simulation results across runs
    random.seed(42)
    main()