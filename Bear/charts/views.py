# from django.views.generic import TemplateView
# from chartjs.views.lines import BaseLineChartView
#
# # Create your views here.
#
# class LineChartJSONView(BaseLineChartView):
#     def get_labels(self):
#         """Return 7 labels for the x-axis."""
#         return ["January", "February", "March", "April", "May", "June", "July"]
#
#     def get_providers(self):
#         """Return names of datasets."""
#         return ["Central", "Eastside", "Westside"]
#
#     def get_data(self):
#         """Return 3 datasets to plot."""
#
#         return [[75, 44, 92, 11, 44, 95, 35],
#                 [41, 92, 18, 3, 73, 87, 92],
#                 [87, 21, 94, 3, 90, 13, 65]]
#
# line_chart_json = LineChartJSONView.as_view()