import sys
from streamlit.web import cli as stccli

sys.argv = ["streamlit", "run", "app.py"]
sys.exit(stccli.main())
