## SecuML
## Copyright (C) 2016-2017  ANSSI
##
## SecuML is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## SecuML is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License along
## with SecuML. If not, see <http://www.gnu.org/licenses/>.

from flask import send_file

from SecuML_web.base import app
from SecuML_web.base.views.experiments import updateCurrentExperiment

from SecuML.Experiment.DescriptiveStatisticsExperiment import DescriptiveStatisticsExperiment

@app.route('/getFeaturesTypes/<experiment_id>/')
def getFeaturesTypes(experiment_id):
    experiment = updateCurrentExperiment(experiment_id)
    filename  = experiment.getOutputDirectory()
    filename += 'features_types.json'
    return send_file(filename)

@app.route('/getStatsPlot/<experiment_id>/<plot_type>/<feature>/')
def getStatsPlot(experiment_id, plot_type, feature):
    experiment = updateCurrentExperiment(experiment_id)
    filename  = experiment.getOutputDirectory() + feature + '/'
    if plot_type.find('histogram') >= 0:
        filename += plot_type + '.json'
    else:
        filename += plot_type + '.png'
    return send_file(filename)
