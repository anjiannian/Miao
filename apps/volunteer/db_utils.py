import models

def get_operators_schools(volunteer_id):
    regions = models.OperatorRegion.objects.filter(operator=volunteer_id)
    schools_in_region = {}
    for region in regions:
        for s in region.schools.all():
            schools_in_region[s.id] = ""

    return schools_in_region.keys()


def get_group_leader_schools(vol_obj):
    result = {}
    groups = models.VolunteerGroup.objects.filter(group_leader=vol_obj)
    for group in groups:
        result[group.school_for_work.id] = ""
    return result.keys()


def get_vol_schools(vol_obj):
    result = {}
    groups = vol_obj.volunteer_groups.all()
    for group in groups:
        result[group.school_for_work.id] = ""
    return result.keys()