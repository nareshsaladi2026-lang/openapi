"""Generate sample response JSON files derived directly from each endpoint's schema."""
import json, os, re

os.makedirs("samples/HUH_edi", exist_ok=True)
os.makedirs("samples/HUH_ipc", exist_ok=True)
os.makedirs("samples/HUH_INTG_Search", exist_ok=True)

# ── value hints: keyword → sample value ──────────────────────────────────────
STR_HINTS = {
    "global_unique_id":              "EDI-HUH-20260608-001",
    "interchange_control_id":        "000001234",
    "interchange_sender_id":         "HUHTAMAKI",
    "interchange_receiver_id":       "WALMART",
    "van_trading_partner_name":      "WALMART",
    "po_number":                     "4500012345",
    "customer_po_number":            "4500012345",
    "order_po_number":               "4500012345",
    "order_number":                  "SO-20260608-001",
    "huhtamaki_order_number":        "SO-20260608-001",
    "invoice_number":                "INV-20260608-001",
    "asn_number":                    "ASN-20260608-001",
    "shipment_identification":       "SHIP-20260607-001",
    "shipment_identification_number":"SHIP-20260607-001",
    "batch":                         "BATCH-20260608-001",
    "runid":                         "9001",
    "integration_run_id":            9001,
    "direction":                     "OB",
    "status":                        "SUCCESS",
    "load_status":                   "DISPATCHED",
    "shipment_status":               "IN_TRANSIT",
    "assign_status":                 "ASSIGNED",
    "so_freight_status":             "SENT",
    "so_release_status":             "RELEASED",
    "so_submit_status":              "SUBMITTED",
    "so_update_status":              "UPDATED",
    "error_msg":                     "",
    "err_msg":                       "",
    "error_message":                 "",
    "error_messages":                "",
    "int_message":                   "SUCCESS",
    "int_messages":                  "SUCCESS",
    "carrier":                       "RYDER",
    "carrier_code":                  "RYDER",
    "carrier_name":                  "Ryder Transportation",
    "shipment_carrier_name":         "Ryder Transportation",
    "standard_carrier_alpha_code":   "RDWY",
    "interline_standard_carrier_alpha_code": "RDWY",
    "shipment_standard_carrier_alpha_code":  "RDWY",
    "transportation_method":         "TL",
    "transportation_means":          "TL",
    "means_code":                    "TL",
    "means_of_transportation":       "TL",
    "freight_terms":                 "PREPAID",
    "shipment_method_paymentcode":   "PP",
    "shipment_method_payment":       "PP",
    "payment_method":                "PREPAID",
    "currency_code":                 "USD",
    "invoice_type":                  "DR",
    "invoice_purpose_code":          "00",
    "invoice_terms_code":            "NET30",
    "invoice_terms_description":     "Net 30 Days",
    "invoice_terms_net_days":        "30",
    "invoice_terms_discount_percent":"0.00",
    "invoice_terms_discount_days_due":"0",
    "invoice_terms_discount_due_date":"",
    "invoice_terms_due_date":        "2026-07-08",
    "po_date":                       "2026-06-01",
    "order_date":                    "2026-06-08",
    "invoice_date":                  "2026-06-08",
    "ship_date":                     "2026-06-07",
    "deliver_date":                  "2026-06-10",
    "delivery_date":                 "2026-06-10",
    "departure_date":                "2026-06-09",
    "run_date":                      "2026-06-08",
    "actual_delivery_date":          "2026-06-10",
    "actual_ship_date":              "2026-06-07",
    "pick_up_date":                  "2026-06-09",
    "pick_up_date_utc":              "2026-06-09",
    "pick_up_time":                  "06:00",
    "pick_up_time_utc":              "11:00",
    "delivery_time":                 "14:00",
    "delivery_time_utc":             "19:00",
    "departure_time":                "06:00",
    "departure_time_utc":            "11:00",
    "actual_ship_time":              "08:30",
    "ship_time":                     "08:30",
    "time_stamp":                    "2026-06-08T10:30:00.000Z",
    "creation_date":                 "2026-06-08T10:30:00.000Z",
    "created_date":                  "2026-06-08T10:30:00.000Z",
    "created_at":                    "2026-06-08T10:30:00.000Z",
    "last_update_date":              "2026-06-08T10:30:00.000Z",
    "receipt_date":                  "2026-06-10",
    "huhtamaki_item_number":         "HUH-ITEM-001",
    "product_number":                "HUH-ITEM-001",
    "customer_item_number":          "CUST-ITEM-001",
    "item_number":                   "HUH-ITEM-001",
    "item_no":                       "HUH-ITEM-001",
    "item":                          "HUH-ITEM-001",
    "item_description":              "Molded Fiber Plate 10in",
    "case_upc_14_digit":             "10012345678905",
    "edi_unit_upc_14_digit":         "00012345678904",
    "ucc_128_vase_pallet_code":      "00612345678901234560",
    "sscc":                          "00612345678901234560",
    "lot_number":                    "LOT-2026060801",
    "lot_num_lotcontrol":            "Y",
    "lpn":                           "LPN-001",
    "licence_plate_number":          "LPN-001",
    "locator":                       "A-01-01",
    "sub_inventory":                 "FG",
    "subinv":                        "FG",
    "warehouse":                     "GB01",
    "warehouse_code":                "GB01",
    "huhtamaki_warehouse":           "GB01",
    "huhtamaki_facility":            "GB01",
    "org_code":                      "M1",
    "fulfillmentorg_code":           "M1",
    "oracle_ship_from_party_warehouse_code": "GB01",
    "erp_from_org_code":             "M1",
    "erp_dest_org_code":             "WM-DC-6094",
    "site_id":                       "GB01",
    "oic_instance_id":               "OIC-PROD3-001",
    "quantity_ordered":              "500",
    "quantity":                      "500",
    "quantity_uom":                  "CA",
    "unit_of_measure":               "CA",
    "quantity_per_pack":             "50",
    "quantity_shipped":              "500",
    "remaining_qty":                 0,
    "shipped_qty":                   500,
    "load_plan_no":                  "LP-20260608-001",
    "load_number":                   "LOAD-001",
    "load_id":                       "LOAD-001",
    "shipment_load_number":          "LOAD-001",
    "shipment":                      "SHIP-20260607-001",
    "ship_num":                      "SHIP-20260607-001",
    "shipment_bill_of_lading":       "BOL-OB-001",
    "bill_of_landing_number":        "BOL-OB-001",
    "bill_of_lading":                "BOL-OB-001",
    "pro_number":                    "PRO-20260607-001",
    "pro_no":                        "PRO-20260607-001",
    "shipment_pro_number":           "PRO-20260607-001",
    "pro":                           "PRO-20260607-001",
    "tracking_number":               "1Z999AA10123456784",
    "shipment_tracking_number":      "1Z999AA10123456784",
    "seal_number":                   "SEAL-001",
    "shipment_seal_number":          "SEAL-001",
    "trailer_number":                "TRL-001",
    "shipment_equipment_number":     "TRL-001",
    "equipment_number":              "TRL-001",
    "equipment_description_code":    "TRL",
    "line_number":                   "1",
    "line_no":                       "1",
    "ship_line_num":                 "1",
    "ship_line_number":              "1",
    "shipment_line_num":             "1",
    "order_line_num":                "1",
    "order_line_number":             "1",
    "stop_no":                       "1",
    "po_order_type":                 "NE",
    "order_type":                    "SO",
    "order_code":                    "SO",
    "erp_order_type":                "SO",
    "order_source":                  "EDI",
    "source_transaction_system":     "ERP",
    "source_transaction_id":         "SO-20260608-001",
    "source":                        "ERP",
    "source_system":                 "ERP",
    "transaction_set_purpose_code":  "00",
    "reference_identification":      "REF-001",
    "routing_sequence_code":         "B",
    "bill_to_party_code":            "HUH-NA",
    "bill_to_party_name":            "Huhtamaki Americas",
    "bill_to_party_duns":            "123456789",
    "bill_to_party_gln":             "0614141000012",
    "bill_to_party_address1":        "2400 Lakeview Pkwy",
    "bill_to_party_address2":        "",
    "bill_to_party_city":            "Alpharetta",
    "bill_to_party_state":           "GA",
    "bill_to_party_postal_code":     "30009",
    "bill_to_party_country":         "US",
    "bill_to_party_province":        "",
    "ship_to_party_code":            "WM-DC-6094",
    "ship_to_party_name":            "Walmart DC 6094",
    "ship_to_party_duns":            "009876543",
    "ship_to_party_gln":             "0614141000029",
    "ship_to_party_address1":        "702 SW 8th St",
    "ship_to_party_address2":        "",
    "ship_to_party_city":            "Bentonville",
    "ship_to_party_state":           "AR",
    "ship_to_party_postal_code":     "72716",
    "ship_to_party_country":         "US",
    "ship_to_party_province":        "",
    "ship_from_party_code":          "GB01",
    "ship_from_party_name":          "Huhtamaki Green Bay",
    "ship_from_party_duns":          "111222333",
    "ship_from_party_gln":           "0614141000098",
    "ship_from_party_address1":      "1919 S. Broadway",
    "ship_from_party_address2":      "",
    "ship_from_party_city":          "Green Bay",
    "ship_from_party_state":         "WI",
    "ship_from_party_postal_code":   "54304",
    "ship_from_party_country":       "US",
    "ship_from_party_province":      "",
    "vendor_party_code":             "HUH-VENDOR-001",
    "vendor_party_name":             "Huhtamaki Americas",
    "vendor_party_duns":             "111222333",
    "vendor_party_gln":              "0614141000098",
    "vendor_party_address1":         "2400 Lakeview Pkwy",
    "vendor_party_address2":         "",
    "vendor_party_city":             "Alpharetta",
    "vendor_party_state":            "GA",
    "vendor_party_postal_code":      "30009",
    "vendor_party_country":          "US",
    "vendor_party_province":         "",
    "vendor_number":                 "HUH-VENDOR-001",
    "vendor_name":                   "Huhtamaki Americas",
    "oracle_bill_to_party_customer_number":  "CUST-001",
    "oracle_ship_to_party_customer_number":  "CUST-002",
    "oracle_order_number":           "SO-20260608-001",
    "huhtamaki_market":              "NA",
    "business_unit":                 "NA",
    "department_number":             "DEPT-001",
    "merchandise_type_code":         "BULK",
    "release_number":                "",
    "appointment_number":            "APPT-001",
    "total_amount":                  "6250.00",
    "unit_price":                    "12.50",
    "line_amount":                   "6250.00",
    "shipping_charge":               "1425.00",
    "total_cost":                    "1425.00",
    "line_haul_rate":                "2.85",
    "flatrate":                      0,
    "freight_multiplier":            1.05,
    "allowance_charge_code":         "C",
    "method_of_handling":            "06",
    "sac_amount":                    "150.00",
    "percent":                       "0.00",
    "description":                   "Freight Charge",
    "note_text":                     "Handle with care",
    "note_type":                     "GEN",
    "shipment_gross_weight":         "5000",
    "shipment_gross_weight_uom":     "LB",
    "weight":                        "5000",
    "weight_uom":                    "LB",
    "load_weight":                   "5000",
    "total_weight":                  "5000",
    "shipment_gross_volume":         "480.5",
    "shipment_gross_volume_uom":     "CF",
    "cube_value":                    "480.5",
    "cube_uom":                      "CF",
    "total_distance":                "210",
    "distance_uom":                  "MI",
    "shipment_pallet_lading_quantity":"10",
    "shipment_container_lading_quantity":"10",
    "handling_unit":                 "10",
    "handing_uom":                   "PLT",
    "number_of_std_pallets":         "8",
    "number_of_chep_pallets":        "2",
    "chep_pallet_count":             "2",
    "ltl_class":                     "85",
    "package_type":                  "PLT",
    "package_level":                 "P",
    "over_under_ship_reason":        "",
    "split_lpn_number":              "",
    "shipment_method":               "TL",
    "acknowledgement_type":          "AC",
    "promised_ship_date":            "2026-06-09",
    "quantity_acknowledged":         "500",
    "quantity_uom_ack":              "CA",
    "originating_city":              "Green Bay",
    "originating_state":             "WI",
    "originating_zip":               "54304",
    "destination_city":              "Bentonville",
    "destination_name":              "Walmart DC 6094",
    "destination_state":             "AR",
    "destination_zip":               "72716",
    "file_id":                       5001,
    "file_header_id":                5001,
    "file_name":                     "RYDER_LP_20260608_001.txt",
    "record_id":                     10001,
    "record_key":                    "RK-20260608-001",
    "unique_id":                     "AAABcDEFGHIJKLM",
    "group_id":                      "GRP-001",
    "total_count":                   1,
    "total_quantity":                500,
    "load_plan_count_per_file":      1,
    "order_nos":                     "SO-20260608-001",
    "order_nos_col":                 "SO-20260608-001",
    "created_by":                    "OIC_INTG",
    "receipt_number":                "RCV-001",
    "attribute1":                    "",
    "huhtamaki_item_ean":            "5012345678904",
    "po_release_number":             "",
    "integration_code":              "HUH_OB_856",
    "integration_name":              "HUH OB ASN to Walmart 856",
    "rice_object":                   "I",
    "success_runs":                  48,
    "fail_runs":                     2,
    "total_runs":                    50,
    "success_percentage":            96.0,
    "difference":                    2,
    "success_records":               97,
    "fail_records":                  3,
    "total_records":                 100,
    "diffrence":                     3,
    "success_percentage_rec":        97.0,
    "tbd1":                          "",
    "tbd2":                          "",
    "tbd3":                          "",
    "tbd4":                          "",
    "tbd5":                          "",
    "tbd6":                          "",
    "tbd7":                          "",
    "tbd8":                          "",
    "tbd9":                          "",
    "tbd10":                         "",
    "date_tbd1":                     "",
    "date_tbd2":                     "",
    "date_tbd3":                     "",
    "tbd_reference_number1":         "",
    "tbd_reference_number2":         "",
    "tbd_reference_number3":         "",
    "tbd_reference_number4":         "",
    "tbd1_from_party_address1":      "",
    "tbd1_from_party_address2":      "",
    "tbd1_from_party_city":          "",
    "tbd1_from_party_country":       "",
    "tbd1_from_party_duns":          "",
    "tbd1_from_party_gln":           "",
    "tbd1_from_party_name":          "",
    "tbd1_from_party_postal_code":   "",
    "tbd1_from_party_province":      "",
    "tbd1_from_party_state":         "",
    "tbd2_from_party_address1":      "",
    "tbd2_from_party_address2":      "",
    "tbd2_from_party_city":          "",
    "tbd2_from_party_country":       "",
    "tbd2_from_party_duns":          "",
    "tbd2_from_party_gln":           "",
    "tbd2_from_party_name":          "",
    "tbd2_from_party_postal_code":   "",
    "tbd2_from_party_province":      "",
    "tbd2_from_party_state":         "",
    "shipment_lading_tbd3":          "",
    "intentionally_blank":           "",
    "last_reason":                   "",
    "attribute_char1":               "",
    "attribute_char2":               "",
    "attribute_char3":               "",
    "attribute_char5":               "",
    "so_header_id":                  200456,
    "action_request_id":             100123,
    "is_freight_flat":               "N",
    "payment_terms":                 "NET30",
    "transportation_terms":          "PREPAID",
    "quantity_of_pallets_shipped":   "10",
    "create_at":                     "Y",
    "int_run_id":                    9001,
    "error_dtl":                     "",
    "requested_uom_code":            "CA",
    "secondary_uom_code":            "EA",
    "original_lpn_number":           "LPN-001",
    "ship_date_hdr":                 "2026-06-07",
    "transaction_date":              "2026-06-07",
    "ucc_128":                       "00612345678901234560",
    "number_of_pallets":             "10",
    "seal_num":                      "SEAL-001",
    "order_number_main":             "SO-20260608-001",
    "shipment_method_pay":           "PP",
    "message_out":                   "Update successful",
    "status_out":                    "SUCCESS",
    "updated_out":                   1,
    "assign_status_put":             "ASSIGNED",
}

def sample_value(field, ftype):
    if field in STR_HINTS:
        return STR_HINTS[field]
    if ftype == "number":
        return 0
    # smart fallbacks on keywords in field name
    f = field.lower()
    if "date" in f:      return "2026-06-08"
    if "time" in f:      return "08:00"
    if "amount" in f or "price" in f or "cost" in f or "rate" in f or "charge" in f:
        return "0.00"
    if "qty" in f or "quantity" in f or "count" in f or "weight" in f or "volume" in f:
        return "0"
    if "number" in f or "_id" in f or "_no" in f:
        return ""
    if "status" in f:    return ""
    if "code" in f:      return ""
    if "name" in f:      return ""
    if "address" in f:   return ""
    return ""

def build_sample(props, schemas, spec_name=""):
    out = {}
    for field, ref_or_schema in props.items():
        if "$ref" in ref_or_schema:
            sname = ref_or_schema["$ref"].split("/")[-1]
            schema = schemas[sname]
        else:
            schema = ref_or_schema
        ftype = schema.get("type", "string")
        # array of items → wrap in items list
        if ftype == "array":
            inner_props = schema.get("items", {}).get("properties", {})
            if inner_props:
                out[field] = [build_sample(inner_props, schemas, spec_name)]
            else:
                out[field] = []
        else:
            v = sample_value(field, ftype)
            if ftype == "number" and isinstance(v, str):
                try: v = float(v) if "." in v else int(v)
                except: v = 0
            out[field] = v
    return out

def path_to_filename(path):
    return path.strip("/").replace("/", "_")

def process_spec(spec_file, out_dir):
    with open(spec_file) as f:
        spec = json.load(f)
    schemas = spec["components"]["schemas"]
    spec_name = spec_file.replace(".json", "")
    count = 0
    for path, methods in spec["paths"].items():
        for method, op in methods.items():
            if method not in ("get", "post", "put"):
                continue
            for code in ("200", "201"):
                if code not in op.get("responses", {}):
                    continue
                content = op["responses"][code].get("content", {}).get("application/json")
                if not content:
                    continue
                schema = content.get("schema", {})
                props = schema.get("properties", {})
                if not props:
                    continue
                sample = build_sample(props, schemas, spec_name)
                fname = path_to_filename(path)
                if method != "get":
                    fname += f"_{method}"
                out_path = f"{out_dir}/{fname}.json"
                with open(out_path, "w") as f:
                    json.dump(sample, f, indent=2)
                content["example"] = sample
                count += 1
                print(f"  {method.upper()} {path}  →  {out_path}")
    with open(spec_file, "w") as f:
        json.dump(spec, f, indent=4)
    print(f"  [{spec_file}] {count} samples written\n")

process_spec("HUH_edi.json",         "samples/HUH_edi")
process_spec("HUH_ipc.json",         "samples/HUH_ipc")
process_spec("HUH_INTG_Search.json", "samples/HUH_INTG_Search")
print("Done.")
