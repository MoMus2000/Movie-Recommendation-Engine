from model import MODEL, DATA, get_id, generate_top_10_values, HINDI_MODEL,HINDI_DATA



def process_result(search_query,hindi=False):
	if(hindi):
		top_10_ids=get_id(HINDI_DATA,search_query,hindi)
	else: 
		top_10_ids = get_id(DATA,search_query,hindi)
	if(len(top_10_ids) == 0):
		return [],[]
		
	if(hindi):
		list_top_10,title = generate_top_10_values(top_10_ids[0],HINDI_MODEL,HINDI_DATA,hindi)
	else:
		list_top_10,title = generate_top_10_values(top_10_ids[0],MODEL,DATA,hindi)
	return list_top_10,title

