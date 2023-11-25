from model import MODEL, DATA, get_id, generate_top_10_values


def process_result(search_query):
	top_10_ids = get_id(DATA,search_query)
	if(len(top_10_ids) == 0):
		return [],[]
		
	list_top_10,title = generate_top_10_values(top_10_ids[0],MODEL,DATA)
	return list_top_10,title

