# Pro-Stat LoL

This project is a Django-based web application designed to interact with the Riot Games API, providing users with personalized statistics and information about their League of Legends gameplay.

## Key Features

1. **Personal Riot Games Developer Token Integration**:
   - Users can input their personal Riot Games developer token to make requests to the Riot Games API.
   - To obtain a token, create an account on the [Riot Games Developer Portal](https://developer.riotgames.com/).
   - After acquiring the token, navigate to the main page of the application and input your token.

2. **Summoner Mastery Points Retrieval**:
   - Users can search for a summoner by their name and retrieve mastery points for each champion.
   - To use this feature:
     - Go to the main page.
     - Enter the summoner's name and region tag (e.g., EUW, NA).
     - Select the "Masteries" option.
     - A pre-filled field is available as an example.
     - *Note: The application uses the EUW server by default.*

3. **Summoner Match History**:
   - Users can search for a summoner by their name and access their recent match history.
   - To use this feature:
     - Go to the main page.
     - Enter the summoner's name and region tag.
     - Select the "Matches" option.
     - A pre-filled field is available as an example.
     - *Note: The application uses the EUW server by default.*

## Technical Details

- **Python Version**: 3.12
- **Docker Integration**:
  - The application runs within a Docker container for ease of deployment.
- **Dependencies**:
  - All required packages are listed in the `requirements.txt` file.
- **Branch Protection**:
  - The `main` branch is protected. Direct pushes are not allowed.
  - To contribute:
    - Create a new branch.
    - Submit a pull request.
    - Await code review and approval.

## Important Notes

- **API Token Validity**:
  - The Riot Games API token is valid for 24 hours. Ensure you regenerate and update your token regularly to maintain functionality.

## Getting Started (TAGED VERSION)

   ```bash
   docker run -p 8000:8000 mathieupro/pro-stat-lol:[tag]
   ```

## Getting Started (Local Development)

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mathieu-ui/pro-stat-lol.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd pro-stat-lol
   ```
3. **Build and Run the Docker Container**:
   ```bash
   docker build -t pro-stat-lol .
   docker run -p 8000:8000 pro-stat-lol
   ```
4. **Access the Application**:
   - Open your browser and navigate to `http://localhost:8000`.

---

## Getting API Token

Go to : https://developer.riotgames.com/ and login with the following creds :

Username : Protateur<br>
Password : XwBpquEvez$0wqX^Fq6bcvrSU

At top right corner on "my account" -> "dashboard" you can claim the token.

YOU MUST REGENERATE THE TOKEN BEFORE COPYING IT.

## Automated tests

In order to test the app we're using Selenium to check if the 2 features are working.<br>
When Selenium finds a hidden html element with the ID "flag" the test is OK.<br>
This html element is on the web page only if there are no error during the request process.<br>
Commited token is expired the tests will fail.
