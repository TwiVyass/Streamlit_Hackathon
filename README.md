# Streamlit_Hackathon
This is a functioning connection that I designed for Streamlit's Connection Hackathon. It uses st.experimental_connections extending to  ExperimentalBaseConnection. My streamlit webpage connects to a Musixmatch API and generates the top-five songs based on the country code you enter. The top-5 songs may or may not be updated depending on Musixmatch

A functional Connection is one that:
1. Connects to a data source or API (other than SQLAlchemy, Snowpark, Google Sheets, and fsspec-compatible data sources like AWS S3, GCP, …).
2. Follows connection-building best practices 186 and include:
          -> A _connect() method to set up and return the underlying connection object
          -> A way to retrieve the underlying connection object (such as a cursor() method)
          -> Convenience methods — at a minimum, a query() method wrapped in @st.cache_data
