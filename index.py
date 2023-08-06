import things
import argparse

def get_areas(area_tag):
    return things.areas(tag=area_tag, include_items=True)

def count_incomplete_tasks(projects):
    count = 0
    for project in projects:
        count += sum(1 for task in project['items'] if task['status'] == 'incomplete' and not (task['start'] == 'Someday' and task['start_date'] is None))
    return count

def generate_output(areas, short_mode=False):
    total_all_areas_incomplete = 0
    for area in areas:
        projects = area['items']
        total_incomplete = count_incomplete_tasks(projects)
        total_all_areas_incomplete += total_incomplete

        if short_mode:
            print(f"Area: '{area['title']}' - Total incomplete: {total_incomplete}")
        else:
            print(f"Area: '{area['title']}'")
            print(f"Total incomplete: {total_incomplete}")
            print("Projects:")
            for project in projects:
                project_incomplete = sum(1 for task in project['items'] if task['status'] == 'incomplete' and not (task['start'] == 'Someday' and task['start_date'] is None))
                print(f"- {project['title']} ({project_incomplete})")
            print("\n")
    
    print(f"Total incomplete tasks in all areas: {total_all_areas_incomplete}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", nargs='?', default='long', choices=['long', 'short'], help="Specify the script execution mode (long or short)")
    args = parser.parse_args()

    work_tag = '🛠 Arbeit'
    private_tag = '💪 Ich'
    work_areas = get_areas(work_tag)
    private_areas = get_areas(private_tag)

    if args.mode == 'short':
        print(work_tag)
        generate_output(work_areas, short_mode=True)
        print("\n")
        print(private_tag)
        generate_output(private_areas, short_mode=True)
    else:
        print(work_tag)
        generate_output(work_areas)
        print("\n")
        print(private_tag)
        generate_output(private_areas)
