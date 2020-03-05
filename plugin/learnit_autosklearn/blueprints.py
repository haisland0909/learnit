class ClassifierCatalog:
    level1 = ["libsvm_svc", "sgd"]
    level2 = level1 + ["random_forest", "gradient_boosting"]
    level3 = None

# Individual classifiers for multi-class classification


class MultiClassifierCatalog:
    level1 = ["libsvm_svc", "sgd"]
    level2 = level1 + ["random_forest", "gradient_boosting"]
    level3 = None


class RegressorCatalog:
    level1 = ["ridge_regression", "liblinear_svr"]
    level2 = level1 + ["random_forest", "gradient_boosting"]
    level3 = None