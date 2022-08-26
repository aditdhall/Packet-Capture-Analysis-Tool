def compute(packets,ipAddr) :
	print 'called compute function in compute_metrics.py'

	totalReqSent = 0
	totalReqReceived = 0
	totalReplySent = 0
	totalReplyReceived = 0

	totalEchoBytesSent = 0
	totalEchoBytesReceived = 0

	totalEchoPayloadSent = 0
	totalEchoPayloadReceived = 0

	replyDelay = 0
	hopCount = 0
	
	pingRTT = 0
	index = 0

	i = 0
	#Calculate info for every pair of packets.
	while i < len(packets)/2:
		i+=1
		# Check if node is on the same network, if it is add 1 to hop count, else take absolute value of request packet minus reply packet then add it to total hopCount
		if packets[index:index+2][1].split()[11].split("=")[1] == packets[index:index+2][0].split()[11].split("=")[1]:
				#print("node is on same network, adding 1 to hop count")
				hopCount += 1
				#print hopCount
		else:
				#print("node is not on same network")
				#hopCount += int(packets[index:index+2][0].split()[11].split("=")[1])
				hopCount += abs(float(packets[index:index+2][0].split()[11].split("=")[1]) - float(packets[index:index+2][1].split()[11].split("=")[1])) +1
		
		#f this packet is the source and request is in the header- then calculate info based about request packet, else calculate info on the reply packet.
		if ipAddr in packets[index:index+2][0].split()[2] and "request" in packets[index:index+2][0].split()[8]:
			#print("This node is the source of an echo request")
			totalReqSent+=1 #Metric 1
			totalReplyReceived+=1 #Metric 4
			totalEchoBytesSent += int(packets[index:index+2][0].split()[5]) #Metric 5

			totalEchoPayloadSent += int(packets[index:index+2][0].split()[5])-42 #Metric 7
			pingRTT += float(packets[index:index+2][1].split()[1]) - float(packets[index:index+2][0].split()[1]) #Time Metric 1

			
		else:
			#print("this node is receiving an echo request")
			totalReqReceived+=1 #Metric 2
			totalReplySent+=1 #Metric 3

			totalEchoBytesReceived += int(packets[index:index+2][0].split()[5]) #Metric 6
			totalEchoPayloadReceived += int(packets[index:index+2][1].split()[5])-42 #Metric 8
			
			replyDelay += float(packets[index:index+2][1].split()[1]) - float(packets[index:index+2][0].split()[1]) #Time Metric 4

		index+=2

	#Print out all info
	print("Total Request Sent: " + str(totalReqSent) + "\nTotal Request Received: " + str(totalReqReceived)) 
	print("Total Replies Sent: " + str(totalReplySent) + "\nTotal Replies Received: " + str(totalReplyReceived))
	print("Total Echo Bytes sent : " + str(totalEchoBytesSent) + "\nTotal Echo Bytes received: " + str(totalEchoBytesReceived))
	
	print("Total Echo Request data sent: " + str(totalEchoPayloadSent) + "\nTotal Echo request data received: " + str(totalEchoPayloadReceived))
	averageRTT = float(pingRTT) / (totalReplyReceived + totalReplySent)
	#Average RTT is wrong according to Garrets example info
	print ("Average RTT: %.2f ms" % (averageRTT*1000))
	
	print("Echo request Throughput: %.1f" % round((totalEchoBytesSent/pingRTT)/1000,1)) #Time Metric 2
	print("Echo request Goodput: %.1f" % round((totalEchoPayloadSent/pingRTT)/1000,1)) #Time Metric 3
	print("Average Reply Delay: %.2f us" % round((replyDelay/totalReplySent)*1000000,2))

	# Average hops per echo isn't correct according to Garrets example info.

	#print("Hop count total: %.2f " % round((hopCount),2))
	print("Average hops per echo: %.2f" % round((hopCount/(totalReqReceived+totalReqSent)),2)) #Distance Metric
	print ("\n")