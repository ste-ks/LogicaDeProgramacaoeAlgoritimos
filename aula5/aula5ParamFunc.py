def contorno (nome):
    try:
        print(f'+ {"-" * len(nome)} +')
        print(f'| {nome} |')
        print(f'+ {"-" * len(nome)} +')
    except Exception as e:
        print(f"An error occurred: {e}")

contorno()

def alarmCleared(tag, tagPath, alarmName, alarmEvent, alarmPath, missedEvents):
	#Calculate duration
	startTime = alarmEvent.activeData.getTimestamp()
	endTime = alarmEvent.clearedData.getTimestamp()
	duration = endTime - startTime
	
	#Filter Long running alarms
	if duration > 5000:
		system.tag.writeAsync('[default]TotalTimeActive', duration)