from project_deepika.input import input_dict_list

with open("output.py", "w") as file_obj:

    input_list_len = len(input_dict_list)

    # Generate a list of inflow
    inflow_list = [input_dict["inflow"] for input_dict in input_dict_list]
    # Calculate the cumulative inflow
    cumulative_inflow_list = [sum(inflow_list[0:counter+1]) for counter in range(input_list_len)]
    print(cumulative_inflow_list)

    # Generate a list of outflow
    outflow_list = [input_dict["outflow"] for input_dict in input_dict_list]
    # Calculate the cumulative inflow
    cumulative_outflow_list = [sum(outflow_list[0:counter+1]) for counter in range(input_list_len)]
    print(cumulative_outflow_list)

    output_list = [cumulative_inflow_list[counter] - cumulative_outflow_list[counter]
                   for counter in range(input_list_len)]
    print(output_list)