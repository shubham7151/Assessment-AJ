import os
import json
from app.test.test_util import datamapper as dm 


def evaluationService(data_type):
    """
    Method evaluates the actual and test response and returns the result

    Args:
        data_types (str): The type of evaluation you need to do.

    Retruns: 
        A JSON response containing the completeness and accuracy of fetched documents
    """
    if data_type == "actual":

        base_dir = os.path.dirname(os.path.abspath(__file__))
        fetch_dir_actual = os.path.abspath(os.path.join(base_dir, "./../responses/actual_data_response.json"))
        
        
        with open(fetch_dir_actual, "r") as actual:
            actual_response = json.load(actual)
        
        fetch_dir_expected = os.path.abspath(os.path.join(base_dir, "../test/test_data/expected_response_actual_data.json"))
        
        with open(fetch_dir_expected, "r") as actual:
            expected_response = json.load(actual)
    elif data_type == "test" :
        base_dir = os.path.dirname(os.path.abspath(__file__))
        fetch_dir_actual = os.path.abspath(os.path.join(base_dir, "../responses/test_data_response.json"))
    
        
        with open(fetch_dir_actual, "r") as actual:
            actual_response = json.load(actual)
        
        fetch_dir_expected = os.path.abspath(os.path.join(base_dir, "../test/test_data/expected_response_test_data.json"))
        with open(fetch_dir_expected, "r") as actual:
            expected_response = json.load(actual)                               

    
    complete =  dm.validateNominatedBankAccount(expected_response["NominatedBankAccount"],actual_response["NominatedBankAccount"]) ["completeness"]+ \
    dm.validateSecurityInformation(expected_response["SecurityInformation"],actual_response["SecurityInformation"]) ["completeness"]+ \
    dm.validateTrusteeDetailsDetails(expected_response["TrusteeDetails"],actual_response["TrusteeDetails"])["completeness"]+ \
    dm.validateBeneficiaryDetails(expected_response["BeneficiaryDetails"],actual_response["BeneficiaryDetails"])["completeness"]+\
    dm.validateTrustRegistrationDetails(expected_response["TrustRegistrationDetails"],actual_response["TrustRegistrationDetails"])["completeness"] +\
    dm.validateDataPrivacyStatement(expected_response["DataPrivacyStatement"],actual_response["DataPrivacyStatement"]) ["completeness"]+\
    dm.validateDonorDetails(expected_response["DonorDetails"],actual_response["DonorDetails"]) ["completeness"]

    acc = dm.validateNominatedBankAccount(expected_response["NominatedBankAccount"],actual_response["NominatedBankAccount"]) ["accuracy"]+ \
    dm.validateSecurityInformation(expected_response["SecurityInformation"],actual_response["SecurityInformation"]) ["accuracy"]+ \
    dm.validateTrusteeDetailsDetails(expected_response["TrusteeDetails"],actual_response["TrusteeDetails"])["accuracy"]+ \
    dm.validateBeneficiaryDetails(expected_response["BeneficiaryDetails"],actual_response["BeneficiaryDetails"])["accuracy"]+\
    dm.validateTrustRegistrationDetails(expected_response["TrustRegistrationDetails"],actual_response["TrustRegistrationDetails"])["accuracy"] +\
    dm.validateDataPrivacyStatement(expected_response["DataPrivacyStatement"],actual_response["DataPrivacyStatement"]) ["accuracy"]+\
    dm.validateDonorDetails(expected_response["DonorDetails"],actual_response["DonorDetails"]) ["accuracy"]

    return {
        "data" : {
            "NominatedBankAccount": dm.validateNominatedBankAccount(expected_response["NominatedBankAccount"],actual_response["NominatedBankAccount"]),
            "SecurityInformation" : dm.validateSecurityInformation(expected_response["SecurityInformation"],actual_response["SecurityInformation"]),
            "TrusteeDetails" : dm.validateTrusteeDetailsDetails(expected_response["TrusteeDetails"],actual_response["TrusteeDetails"]),
            "BeneficiaryDetails" : dm.validateBeneficiaryDetails(expected_response["BeneficiaryDetails"],actual_response["BeneficiaryDetails"]),
            "TrustRegistrationDetails" : dm.validateTrustRegistrationDetails(expected_response["TrustRegistrationDetails"],actual_response["TrustRegistrationDetails"]),
            "DataPrivacyStatement" : dm.validateDataPrivacyStatement(expected_response["DataPrivacyStatement"],actual_response["DataPrivacyStatement"]),
            "DonorDetails" : dm.validateDonorDetails(expected_response["DonorDetails"],actual_response["DonorDetails"]),

            "Average":{"completeness" : complete/7,
                        "accuracy" : acc/7
                        }
        },
        
    }