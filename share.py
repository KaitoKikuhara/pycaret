#ignore warnings
import warnings
warnings.filterwarnings('ignore')


def save_model(model, model_name, verbose=True):
    model_ = []
    model_.append(prep_pipe)
    model_.append(model)
    import joblib
    model_name = model_name + '.pkl'
    joblib.dump(model_, model_name)
    if verbose:
        print('Transformation Pipeline and Model Succesfully Saved')



def save_experiment(experiment_name=None):


    """

    Description:
    ------------
    This function saves the entire experiment into the current active directory.
    All outputs using pycaret are internally saved into a binary list which is
    pickilized when save_experiment() is used.

        Example:
        --------
        save_experiment()

        This will save the entire experiment into the current active directory. By
        default, the name of the experiment will use the session_id generated during
        setup(). To use a custom name, a string must be passed to the experiment_name
        param. For example:

        save_experiment('experiment_23122019')

    Parameters
    ----------
    experiment_name : string, default = none
    Name of pickle file to be passed as a string.

    Returns:
    --------
    Success Message

    Warnings:
    ---------
    None


    """

    #ignore warnings
    import warnings
    warnings.filterwarnings('ignore')

    #general dependencies
    import joblib
    global experiment__

    #defining experiment name
    if experiment_name is None:
        experiment_name = 'experiment_' + str(seed)

    else:
        experiment_name = experiment_name

    experiment_name = experiment_name + '.pkl'
    joblib.dump(experiment__, experiment_name)

    print('Experiment Succesfully Saved')



def load_experiment(experiment_name):

    """

    Description:
    ------------
    This function loads a previously saved experiment from the current active
    directory into current python environment. Load object must be a pickle file.

        Example:
        --------
        saved_experiment = load_experiment('experiment_23122019')

        This will load the entire experiment pipeline into the object saved_experiment.
        The experiment file must be in current directory.

    Parameters
    ----------
    experiment_name : string, default = none
    Name of pickle file to be passed as a string.

    Returns:
    --------
    Information Grid containing details of saved objects in experiment pipeline.

    Warnings:
    ---------
    None


    """

    #ignore warnings
    import warnings
    warnings.filterwarnings('ignore')

    #general dependencies
    import joblib
    import pandas as pd

    experiment_name = experiment_name + '.pkl'
    temp = joblib.load(experiment_name)

    name = []
    exp = []

    for i in temp:
        name.append(i[0])
        exp.append(i[-1])

    ind = pd.DataFrame(name, columns=['Object'])
    display(ind)

    return exp
