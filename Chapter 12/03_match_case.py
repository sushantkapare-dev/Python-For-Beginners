def http_status(status):
    match status:
        case 200:
            return 'OK'
        case 300:
            return 'Multiple Choices'
        case 400:
            return 'Bad Request'
        case 401:
            return 'Unauthorized'
        case 402:
            return 'Payment Required'
        case 500:
            return 'Internal Server Error'
        case _:
            return 'Unknown status'
        
print(http_status(50007))
        