import json
from .test_util import datamapper as dm 
import os 

def test_actual_response():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fetch_dir_actual = os.path.abspath(os.path.join(base_dir, "./../responses/actual_data_response.json"))
    
    
    with open(fetch_dir_actual, "r") as actual:
        actual_response = json.load(actual)
    
    fetch_dir_expected = os.path.abspath(os.path.join(base_dir, "./test_data/expected_response_actual_data.json"))
    
    with open(fetch_dir_expected, "r") as actual:
        expected_response = json.load(actual)

    assert dm.validateTrustRegistrationDetails(expected_response["TrustRegistrationDetails"],actual_response["TrustRegistrationDetails"]) == {'accuracy': 1.0, 'completeness': 1.0}, "TrustRegistration mismatch"
    assert dm.validateDataPrivacyStatement(expected_response["DataPrivacyStatement"],actual_response["DataPrivacyStatement"]) == {'accuracy': 1.0, 'completeness': 1.0}, "DataPrivacyStatement mismatch"
    assert dm.validateDonorDetails(expected_response["DonorDetails"],actual_response["DonorDetails"]) == {'accuracy': 1.0, 'completeness': 1.0}, "DonorDetails mismatch"
    assert dm.validateNominatedBankAccount(expected_response["NominatedBankAccount"],actual_response["NominatedBankAccount"]) == {'accuracy': 1.0, 'completeness': 1.0}, "NominatedBankAccount mismatch"
    assert dm.validateSecurityInformation(expected_response["SecurityInformation"],actual_response["SecurityInformation"]) == {'accuracy': 1.0, 'completeness': 1.0}, "SecurityInformation mismatch"
    assert dm.validateTrusteeDetailsDetails(expected_response["TrusteeDetails"],actual_response["TrusteeDetails"])=={'accuracy': 1.0, 'completeness': 1.0}, "TrusteeDetails mismatch"
    assert dm.validateBeneficiaryDetails(expected_response["BeneficiaryDetails"],actual_response["BeneficiaryDetails"]) == {'accuracy': 1.0, 'completeness': 1.0}, "BeneficiaryDetails mismatch"
    

def test_dummy_response():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fetch_dir_actual = os.path.abspath(os.path.join(base_dir, "../responses/test_data_response.json"))
    
    
    with open(fetch_dir_actual, "r") as actual:
        actual_response = json.load(actual)
    
    fetch_dir_expected = os.path.abspath(os.path.join(base_dir, "./test_data/expected_response_test_data.json"))
    with open(fetch_dir_expected, "r") as actual:
        expected_response = json.load(actual)

    assert dm.validateTrustRegistrationDetails(expected_response["TrustRegistrationDetails"],actual_response["TrustRegistrationDetails"]) == {'accuracy': 1.0, 'completeness': 1.0}, "TrustRegistration mismatch"
    assert dm.validateDataPrivacyStatement(expected_response["DataPrivacyStatement"],actual_response["DataPrivacyStatement"]) == {'accuracy': 1.0, 'completeness': 1.0}, "DataPrivacyStatement mismatch"
    assert dm.validateDonorDetails(expected_response["DonorDetails"],actual_response["DonorDetails"]) == {'accuracy': 1.0, 'completeness': 1.0}, "DonorDetails mismatch"
    assert dm.validateNominatedBankAccount(expected_response["NominatedBankAccount"],actual_response["NominatedBankAccount"]) == {'accuracy': 1.0, 'completeness': 1.0}, "NominatedBankAccount mismatch"
    assert dm.validateSecurityInformation(expected_response["SecurityInformation"],actual_response["SecurityInformation"]) == {'accuracy': 1.0, 'completeness': 1.0}, "SecurityInformation mismatch"
    assert dm.validateTrusteeDetailsDetails(expected_response["TrusteeDetails"],actual_response["TrusteeDetails"])=={'accuracy': 1.0, 'completeness': 1.0}, "TrusteeDetails mismatch"
    assert dm.validateBeneficiaryDetails(expected_response["BeneficiaryDetails"],actual_response["BeneficiaryDetails"]) == {'accuracy': 1.0, 'completeness': 1.0}, "BeneficiaryDetails mismatch"
