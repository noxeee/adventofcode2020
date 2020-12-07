
lines = importdata("day7_input.txt", "\n");

function dicts = create_dicts(bag_data)
    dicts
    for i = size(bag_data)
        
        split_str = strsplit(bag_data(i), " ")

        main_bag = split_str(1:2)
        
        sub_bags = []

        for j = 5:size(split_str)
            sub_bags = [sub_bags; split_str(j+1:j+2)]
        endfor

        bag_struct = struct("main_bag", main_bag, "sub_bags", sub_bags)

        dicts = [dicts; bag_struct]
    endfor

    return dicts
endfunction


function colour = get_new_colour(pos)
    colour = "";

    return colour
end

function count = find_num_bags(bag_colour)
    count = 0;
    for i = size(lines)
        found_pos = strfind(lines(i), bag_colour)
            if (!isempty(found))
                new_colour = get_new_colour(found_pos)
                count++
                count += find_num_bags(new_colour)
        endif
    endfor

    return count
endfunction


#find(lines)

#strfind()
#strmatch()
