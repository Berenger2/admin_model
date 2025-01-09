from flask import Flask, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os 
from datetime import datetime
 
 
load_dotenv()

app = Flask(__name__)

db_user = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
Session = sessionmaker(bind=engine)

@app.route('/experiences', methods=['GET'])
def get_all_experiences():
    session = Session()
    try:
        query = "SELECT * FROM website_experience"
        result = session.execute(text(query))
        experiences = [row._asdict() for row in result]
        return jsonify(experiences)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/deploiements', methods=['GET'])
def get_all_deploiements():
        session = Session()
        try:
            query = "SELECT * FROM website_deploiement"
            result = session.execute(text(query))
            deploiements = [row._asdict() for row in result]
            return jsonify(deploiements)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            session.close()
        
@app.route('/deploiements/pr', methods=['GET'])
def get_deploiements_pr():
    session = Session()
    try:
        query = "SELECT * FROM website_deploiement WHERE state = 'PR'"
        result = session.execute(text(query))
        deploiements = [row._asdict() for row in result]
        return jsonify(deploiements)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()