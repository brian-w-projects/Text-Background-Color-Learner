from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator, TransformerMixin


class HexToInt(BaseEstimator, TransformerMixin):
    """Custom Transformer to alter string based hex digits into their corresponding int values
    """

    def transform(self, X, y=None):
        return X.applymap(lambda x: int(x, base=16)).astype(float)

    def fit(self, X, y=None):
        return self


def train_model(data):
    """ML pipeline to train font color selection model based on user input.

    Args:
        data (:2d numpy array:): Each row is an r, g, b value and corresponding font color preferences

    Returns:
        Trained scikit learn model
    """

    X_train, X_test, y_train, y_test = train_test_split(
        data.iloc[:, :3], data.iloc[:, 3], random_state=0
    )

    pipeline = make_pipeline(
        HexToInt(),
        StandardScaler(),
        GradientBoostingClassifier()
    )

    param_grid = {
        'gradientboostingclassifier__max_depth': [1, 2, 3],
        'gradientboostingclassifier__n_estimators': [10, 50, 100, 200],
        'gradientboostingclassifier__learning_rate': [0.001, 0.001, 0.01, 0.1, 0.2, 0.3],
    }

    grid = GridSearchCV(pipeline, param_grid=param_grid, cv=5, iid=False)
    grid.fit(X_train, y_train)
    print(f"Learning Ability: {grid.score(X_test, y_test)}")
    return grid
