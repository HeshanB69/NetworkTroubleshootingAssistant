from mac_vendor_lookup import MacLookup

lookup = MacLookup()

try:
    lookup.update_vendors()
except:
    pass


def get_manufacturer(mac):

    try:
        return lookup.lookup(mac)

    except:
        return "Unknown"