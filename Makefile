# ----------------------------------
#         STREAMLIT server COMMANDS
# ----------------------------------

streamlit:
	-@streamlit run app.py

streamlit2:
	-@streamlit run app-v2.py

# ----------------------------------
#    LOCAL INSTALL COMMANDS
# ----------------------------------

clean:
	@rm -fr */__pycache__
	@rm -fr __init__.py
	@rm -fr build
	@rm -fr dist
	@rm -fr *.dist-info
	@rm -fr *.egg-info
	-@rm model.joblib
