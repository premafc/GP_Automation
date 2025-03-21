import psycopg2

def fetch_latest_email_otp_by_email(email):
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="glp",
            user="testing",
            password="gpT3stU$er@2O2iv",
            host="13.201.204.200",
            port="5432"
        )

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Define the query to select the latest email OTP using the id column
        query = """
        SELECT email_otp
        FROM user_kyc_details
        WHERE email_id = %s
        ORDER BY id DESC
        LIMIT 1
        """

        # Execute the query with the email parameter
        cur.execute(query, (email,))

        # Fetch the result
        result = cur.fetchone()

        # Close communication with the database
        cur.close()
        conn.close()

        # If result is None, return None
        if not result:
            print(f"No user found with email_id = '{email}'")
            return None

        email_otp = result[0]

        return email_otp

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def fetch_latest_mobile_otp_by_number(mobile_number):
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="glp",
            user="testing",
            password="gpT3stU$er@2O2iv",
            host="13.201.204.200",
            port="5432"
        )

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Define the query to select the latest mobile OTP using the correct column name
        query = """
        SELECT mobile_otp
        FROM user_kyc_details
        WHERE mobile_no = %s  -- Update 'mobile' to your actual column name if it's different
        ORDER BY id DESC
        LIMIT 1
        """

        # Execute the query with the mobile number parameter
        cur.execute(query, (mobile_number,))

        # Fetch the result
        result = cur.fetchone()

        # Close communication with the database
        cur.close()
        conn.close()

        # If result is None, return None
        if not result:
            print(f"No user found with mobile_number = '{mobile_number}'")
            return None

        mobile_otp = result[0]

        return mobile_otp

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
