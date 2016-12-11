from spyre import server
import pandas as pd
import json


class SpecExample(server.App):

    title = "Spectrogram demo"

    inputs = [{   "type":'dropdown',
                  "label": 'Sample',
                  "options" : [],
                  "key": 'ticker',
                  "action_id": "update_data"},

              {   "type":'dropdown',
                  "label": 'Window',
                  "options" : [],
                  "key": 'ws',
                  "action_id": "update_data"},
              ]

    controls = [{   "type" : "hidden",
                    "id" : "update_data"}]

    tabs = ["Plot", "Table"]

    outputs = [{ "type" : "plot",
                    "id" : "plot",
                    "control_id" : "update_data",
                    "tab" : "Plot"},
                { "type" : "table",
                    "id" : "table_id",
                    "control_id" : "update_data",
                    "tab" : "Table",
                    "on_page_load" : True }]

    def __init__(self, samples, windows, directory):
        options = [{"label": sample, "value": directory + "/" +sample}
            for sample in samples]
        self.inputs[0]["options"] = options

        options = [{"label": W, "value": W} for W in windows]
        self.inputs[1]["options"] = options

    def getData(self, params):
        ticker = params['ticker']
        import soundfile
        sig, samplerate = soundfile.read(ticker + ".wav")
        df = pd.Series({"filename": ticker, "length": len(sig),
            "samplerate": samplerate})
        df = df.to_frame().transpose()
        return df

    def getPlot(self, params):
        self.getData(params)
        ticker = params['ticker']
        ws = params['ws']
        from pylab import imread, imshow, figure, xticks, yticks
        fig = figure()
        imshow(imread(ticker + "_%s.png" % ws))
        xticks([])
        yticks([])
        return fig

    def getCustomCSS(self):
        return ""

if __name__ == "__main__":
    # need to define the input filenames !
    app = SpecExample()
    app.launch(port=9093)
