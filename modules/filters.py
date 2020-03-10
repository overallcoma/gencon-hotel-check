def filter_hotel_room_objects(hotel_room_objects, config):
    if hotel_room_objects:
        hotel_room_object_list = filter_hotel_room_objects_distance(hotel_room_objects, config)
    else:
        return hotel_room_objects
    if config.filter_hotelname:
        if hotel_room_object_list:
            hotel_room_object_list = filter_hotel_room_objects_hotelname(hotel_room_object_list, config)
        else:
            return hotel_room_object_list
    if config.filter_room:
        if hotel_room_object_list:
            hotel_room_object_list = filter_hotel_room_objects_roomkeyword(hotel_room_object_list, config)
        else:
            return hotel_room_object_list
    return hotel_room_object_list


def filter_hotel_room_objects_distance(hotel_room_objects, config):
    filtered_list = []
    for hotel_room in hotel_room_objects:
        if config.search_skywalk:
            if 'Skywalk' in hotel_room.distance:
                filtered_list.append(hotel_room)
        if config.search_blocks or config.search_miles:
            distance_unit = hotel_room.distance.split(" ")[0]
            distance_unit = float(distance_unit)
        if config.search_blocks:
            if 'Block' in hotel_room.distance:
                if distance_unit < config.search_blocks_max:
                    filtered_list.append(hotel_room)
        if config.search_miles:
            if 'Mile' in hotel_room.distance:
                if distance_unit < config.search_miles_max:
                    filtered_list.append(hotel_room)
    return filtered_list


def filter_hotel_room_objects_hotelname(hotel_room_objects, config):
    filtered_list = []
    for hotel_room in hotel_room_objects:
        if config.filter_hotelname_keyword in hotel_room.name:
            filtered_list.append(hotel_room)
    return filtered_list


def filter_hotel_room_objects_roomkeyword(hotel_room_object_list, config):
    filtered_list = []
    for hotel_room in hotel_room_object_list:
        if config.filter_room_include in hotel_room.roomtype:
            if config.filter_room_exclude not in hotel_room.roomtype:
                filtered_list.append(hotel_room)
    return filtered_list
