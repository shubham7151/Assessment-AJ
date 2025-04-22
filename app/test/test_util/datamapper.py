

def validateTrustRegistrationDetails(expected,actual):
    not_accuracy = []
    not_completeness = []
    for key in expected.keys():
        if key not in actual.keys():
            not_completeness.append(key)
        elif expected[key] != actual[key]:
                not_accuracy.append(key)
    return {
        "accuracy" : 1 - (len(not_accuracy) / len(expected.keys())),
        "completeness" : 1 - (len(not_completeness) / len(expected.keys()))
    }
    
def validateTrusteeDetailsDetails(expected, actual):
    not_accuracy = []
    not_completeness = []
    for key in expected.keys():
        if key not in actual.keys():
            not_completeness.append(key)
        else :
            if isinstance(expected[key] , dict):
                for nest_key in expected[key].keys():
                    if nest_key not in actual[key].keys():
                        not_completeness.append(nest_key)
                    else : 
                        if expected[key][nest_key] != actual[key][nest_key]:
                            not_accuracy.append(nest_key)
            elif expected[key] != actual[key] :
                not_accuracy.append(key)
    
    return {
        "accuracy" : 1 - (len(not_accuracy) / len(expected.keys())),
        "completeness" : 1 - (len(not_completeness) / len(expected.keys()))
    }

def validateBeneficiaryDetails(expected, actual):
    not_accuracy = []
    not_completeness = []
    for key in expected.keys():
        if key not in actual.keys():
            not_completeness.append(key)
        else :
            if isinstance(expected[key] , dict):
                for nest_key in expected[key].keys():
                    if nest_key not in actual[key].keys():
                        not_completeness.append(nest_key)
                    else : 
                        if expected[key][nest_key] != actual[key][nest_key]:
                            not_accuracy.append(nest_key)
            elif expected[key] != actual[key] :
                not_accuracy.append(key)
    
    return {
        "accuracy" : 1 - (len(not_accuracy) / len(expected.keys())),
        "completeness" : 1 - (len(not_completeness) / len(expected.keys()))
    }

def validateDataPrivacyStatement(expected, actual):
    not_accuracy = []
    not_completeness = []
    for key in expected.keys():
        if key not in actual.keys():
            not_completeness.append(key)
        else :
            if isinstance(expected[key], list):
                for index,item in enumerate(expected[key]):
                    if isinstance(item , dict):
                        for nest_key in item.keys():
                            if nest_key not in actual[key][index]:
                                not_completeness.append(nest_key)
                            else : 
                                # print(f"actual; {actual[key][index][nest_key]}")
                                # print(f"actusl_key{actual[key]}")
                                if item[nest_key] != actual[key][index][nest_key]:
                                    not_accuracy.append(nest_key)
            elif expected[key] != actual[key] :
                not_accuracy.append(nest_key)
    
    return {
        "accuracy" : 1 - (len(not_accuracy) / len(expected.keys())),
        "completeness" : 1 - (len(not_completeness) / len(expected.keys()))
    }

def validateDonorDetails(expected, actual):
    not_accuracy = []
    not_completeness = []
    for key in expected.keys():
        if key not in actual.keys():
            not_completeness.append(key)
        elif expected[key] != actual[key]:
                not_accuracy.append(key)
    return {
        "accuracy" : 1 - (len(not_accuracy) / len(expected.keys())),
        "completeness" : 1 - (len(not_completeness) / len(expected.keys()))
    }

def validateNominatedBankAccount(expected, actual):
    not_accuracy = []
    not_completeness = []
    for key in expected.keys():
        if key not in actual.keys():
            not_completeness.append(key)
        elif expected[key] != actual[key]:
                not_accuracy.append(key)
    return {
        "accuracy" : 1 - (len(not_accuracy) / len(expected.keys())),
        "completeness" : 1 - (len(not_completeness) / len(expected.keys()))
    }

def validateSecurityInformation(expected, actual):
    not_accuracy = []
    not_completeness = []
    for key in expected.keys():
        if key not in actual.keys():
            not_completeness.append(key)
        else :
            if isinstance(expected[key] , dict):
                for nest_key in expected[key].keys():
                    if nest_key not in actual[key].keys():
                        not_completeness.append(nest_key)
                    else : 
                        
                        if expected[key][nest_key].lower() != actual[key][nest_key].lower():
                            not_accuracy.append(nest_key)
            elif expected[key] != actual[key] :
                not_accuracy.append(key)
    print(not_accuracy)
    return {
        "accuracy" : 1 - (len(not_accuracy) / len(expected.keys())),
        "completeness" : 1 - (len(not_completeness) / len(expected.keys()))
    }