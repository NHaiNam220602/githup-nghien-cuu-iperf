from matplotlib import pyplot
from collections import Counter
import csv
def tcp():
    with open('data.txt', 'r') as txt_file:
            lines = txt_file.readlines()	
            lines = lines[4:]
            lines = [line.replace('3]','') for line in lines]
            lines = [line.replace('MBytes','') for line in lines]
            lines = [line.replace('KBytes','') for line in lines]
            lines = [line.replace('sec','') for line in lines]
            lines = [line.replace('Mbits/','') for line in lines]
            for i, line in enumerate(lines):
                lines[i] = line.replace("-", "- ")
    with open('data.csv', 'w') as csv_file:    
        # Tạo đối tượng csv writer
            writer = csv.writer(csv_file)
        # Duyệt qua từng dòng và ghi vào file .csv
            for line in lines:
                writer.writerow(line.split())
tcp()
def udp():
    with open('b.txt', 'r') as txt_file:
            lines = txt_file.readlines()	
            lines = lines[4:]
            lines = [line.replace('3]','') for line in lines]
            lines = [line.replace('MBytes','') for line in lines]
            lines = [line.replace('KBytes','') for line in lines]
            lines = [line.replace('sec','') for line in lines]
            lines = [line.replace('Mbits/','') for line in lines]
            for i, line in enumerate(lines):
                lines[i] = line.replace("-", "- ")
    with open('b.csv', 'w') as csv_file:    
        # Tạo đối tượng csv writer
            writer = csv.writer(csv_file)
        # Duyệt qua từng dòng và ghi vào file .csv
            for line in lines:
                writer.writerow(line.split())
udp()
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
def read():
    iperf3 = []
    with open('b.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            timer = row['Interval']
            bandwidth = row['Bandwidth']
            iperf.append({'timer': timer,
                        'bandwidth': bandwidth})
    return iperf3
iperf3 = read()
def draw_time_by_bandwidth(iperf,iperf3):
    time = [float(iperf['timer']) for iperf in iperf]
    time3 = [float(iperf3['timer']) for iperf3 in iperf3]
    bandwidths = [float(iperf['bandwidth']) for iperf in iperf]
    bandwidths3 = [float(iperf3['bandwidth']) for iperf3 in iperf3]
    pyplot.plot(time, bandwidths,color='red',linestyle='--',marker='.')
    pyplot.plot(time3, bandwidths3,color='red',linestyle='--',marker='.')
    pyplot.xlabel("Bandwidth(Mbit/sec)")
    pyplot.ylabel("Interval(sec)")
    pyplot.grid(True)
    pyplot.show()
draw_time_by_bandwidth((iperf),(iperf3))

