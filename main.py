from matplotlib import pyplot
from collections import Counter
import csv
def tcp():
    with open('data.txt', 'r') as txt_file:
            lines = txt_file.readlines()	
            lines = [line.replace('3]','') for line in lines]
            lines = [line.replace('MBytes','') for line in lines]
            lines = [line.replace('KBytes','') for line in lines]
            lines = [line.replace('sec','') for line in lines]
            lines = [line.replace('Mbits','') for line in lines]
            lines = [line.replace('/','') for line in lines]
            lines = [line.replace('sec','') for line in lines]
    with open('data.csv', 'w') as csv_file:
        # Tạo đối tượng csv writer
            writer = csv.writer(csv_file)
        # Duyệt qua từng dòng và ghi vào file .csv
            for line in lines:
                writer.writerow(line.split())
tcp()
def read_csv():
    iperf = []
    with open('data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            timer = row['Interval']
            bandwidth = row['Bandwidth']
            iperf.append({'timer': timer,
                        'bandwidth': bandwidth})
    return iperf
iperf = read_csv()
def draw_time_by_bandwidth(iperf):
    time = [float(iperf['timer']) for iperf in iperf]
    bandwidths = [float(iperf['bandwidth']) for iperf in iperf]
    pyplot.plot(time, bandwidths,color='red',linestyle='--',marker='.')
    pyplot.xlabel("Bandwidth(Mbit/sec)")
    pyplot.ylabel("Interval(sec)")
    pyplot.grid(True)
    pyplot.show()
draw_time_by_bandwidth((iperf))

