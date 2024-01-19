from database import database as db


if __name__ == "__main__":

    print("*** Выбор типа обучения ***", end="\n\n")

    entities = db.get_entities_1()  # Get initial set of entities

    # Ask for filters
    duration_filters = ["малая", "средняя", "высокая"]
    duration_filter = input(f"Выберите длительность из: {', '.join(duration_filters)} (или оставьте поле пустым для отсутствия фильтра): ").strip()
    if duration_filter in duration_filters:
        entities = db.filter_by_duration(entities, duration_filter)
    print(entities, end="\n\n")

    # Ask for principle filter
    principle_filters = ["итеративный", "эвристический"]
    principle_filter = input(f"Выберите принцип из: {', '.join(principle_filters)} (или оставьте поле пустым для отсутствия фильтра): ").strip()
    if principle_filter in principle_filters:
        entities = db.filter_by_principle(entities, principle_filter)
    print(entities, end="\n\n")

    # Ask for using_premade filter
    using_premade_filters = ["да", "нет"]
    using_premade_filter = input(f"Фильтровать по использованию готовых решений? {', '.join(using_premade_filters)} (или оставьте поле пустым для отсутствия фильтра): ").strip().lower()
    if using_premade_filter in using_premade_filters:
        using_premade = using_premade_filter == "да"
        entities = db.filter_by_using_premade(entities, using_premade)

    # Print out the filtered entities
    print()
    
    if entities:
        print("Подходящие типы обучения:")
        print(', '.join(entities))
    else:
        print("Ничего не найдено.")
