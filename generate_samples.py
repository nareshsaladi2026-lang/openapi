"""Generate sample response JSON files for all three OpenAPI specs."""
import json, os

os.makedirs("samples/HUH_edi", exist_ok=True)
os.makedirs("samples/HUH_ipc", exist_ok=True)
os.makedirs("samples/HUH_INTG_Search", exist_ok=True)

TS = "2026-06-08T10:30:00.000Z"
DATE = "2026-06-08T00:00:00.000Z"

# ── HUH_edi ──────────────────────────────────────────────────────────────────

samples_edi = {
    "ib_850": {
        "attribute_char1": "STD",
        "attribute_char2": "NET30",
        "attribute_char3": "",
        "attribute_char5": "",
        "bill_to_party_code": "HUH-NA",
        "bill_to_party_duns": "123456789",
        "bill_to_party_gln": "0614141000012",
        "case_upc_14_digit": "10012345678905",
        "customer_item_number": "CUST-ITEM-001",
        "direction": "IB",
        "global_unique_id": "EDI-850-20260608-001",
        "interchange_control_id": "000001234",
        "interchange_receiver_id": "HUHTAMAKI",
        "interchange_sender_id": "WALMART",
        "order_date": "2026-06-08",
        "order_number": "PO-20260608-001",
        "po_number": "4500012345",
        "quantity": "100",
        "quantity_uom": "CA",
        "ship_to_party_code": "DC-001",
        "ship_to_party_gln": "0614141000029",
        "unit_price": "12.50",
        "vendor_code": "HUH-VENDOR-001"
    },
    "ib_856": {
        "actual_ship_date": "2026-06-07",
        "bill_of_lading": "BOL-20260607-001",
        "carrier_code": "UPSN",
        "direction": "IB",
        "global_unique_id": "EDI-856-20260608-001",
        "interchange_control_id": "000001235",
        "interchange_receiver_id": "HUHTAMAKI",
        "interchange_sender_id": "WALMART",
        "item_number": "HUH-ITEM-001",
        "lot_number": "LOT-2026060801",
        "order_number": "PO-20260608-001",
        "po_number": "4500012345",
        "quantity_shipped": "100",
        "quantity_uom": "CA",
        "ship_date": "2026-06-07",
        "shipment_id": "SHIP-20260607-001",
        "tracking_number": "1Z999AA10123456784"
    },
    "ob_204": {
        "batch": "BATCH-20260608-001",
        "carrier_code": "RYDER",
        "direction": "OB",
        "global_unique_id": "EDI-204-20260608-001",
        "interchange_control_id": "000001236",
        "interchange_receiver_id": "RYDER",
        "interchange_sender_id": "HUHTAMAKI",
        "load_plan_no": "LP-20260608-001",
        "order_number": "SO-20260608-001",
        "status": "SENT"
    },
    "ob_204_header": {
        "batch": "BATCH-20260608-001",
        "bill_of_landing_number": "BOL-OB-001",
        "carrier_code": "RYDER",
        "customer_po_number": "4500012345",
        "date_tbd1": "2026-06-09",
        "date_tbd2": "2026-06-10",
        "date_tbd3": "",
        "direction": "OB",
        "global_unique_id": "EDI-204-20260608-001",
        "interchange_control_id": "000001236",
        "interchange_receiver_id": "RYDER",
        "interchange_sender_id": "HUHTAMAKI",
        "load_id": "LOAD-001",
        "load_plan_no": "LP-20260608-001",
        "order_date": "2026-06-08",
        "order_number": "SO-20260608-001",
        "origin_city": "Green Bay",
        "origin_state": "WI",
        "origin_zip": "54301",
        "dest_city": "Chicago",
        "dest_state": "IL",
        "dest_zip": "60601",
        "status": "SENT",
        "total_weight": "5000",
        "weight_uom": "LB"
    },
    "ob_204_lines": {
        "batch": "BATCH-20260608-001",
        "global_unique_id": "EDI-204-20260608-001",
        "item_description": "Molded Fiber Plate 10in",
        "item_number": "HUH-ITEM-001",
        "line_number": "1",
        "load_plan_no": "LP-20260608-001",
        "order_number": "SO-20260608-001",
        "quantity": "500",
        "quantity_uom": "CA",
        "upc": "10012345678905",
        "weight": "2500",
        "weight_uom": "LB"
    },
    "ob_204_notes": {
        "batch": "BATCH-20260608-001",
        "global_unique_id": "EDI-204-20260608-001",
        "load_plan_no": "LP-20260608-001",
        "note_text": "Fragile - handle with care",
        "note_type": "GEN",
        "order_number": "SO-20260608-001"
    },
    "ob_810": {
        "batch": "BATCH-INV-20260608-001",
        "direction": "OB",
        "global_unique_id": "EDI-810-20260608-001",
        "interchange_control_id": "000001237",
        "interchange_receiver_id": "WALMART",
        "interchange_sender_id": "HUHTAMAKI",
        "invoice_number": "INV-20260608-001",
        "order_number": "SO-20260608-001",
        "po_number": "4500012345",
        "status": "SENT",
        "total_amount": "6250.00"
    },
    "ob_810_details": {
        "batch": "BATCH-INV-20260608-001",
        "global_unique_id": "EDI-810-20260608-001",
        "invoice_number": "INV-20260608-001",
        "item_description": "Molded Fiber Plate 10in",
        "item_number": "HUH-ITEM-001",
        "line_amount": "6250.00",
        "line_number": "1",
        "order_number": "SO-20260608-001",
        "po_number": "4500012345",
        "quantity_invoiced": "500",
        "quantity_uom": "CA",
        "unit_price": "12.50"
    },
    "ob_810_header": {
        "appointment_number": "APPT-001",
        "batch": "BATCH-INV-20260608-001",
        "bill_to_party_address1": "702 SW 8th St",
        "bill_to_party_address2": "",
        "bill_to_party_city": "Bentonville",
        "bill_to_party_code": "WALMART-HQ",
        "bill_to_party_country": "US",
        "bill_to_party_duns": "009876543",
        "bill_to_party_name": "Walmart Inc",
        "bill_to_party_state": "AR",
        "bill_to_party_zip": "72716",
        "currency_code": "USD",
        "direction": "OB",
        "global_unique_id": "EDI-810-20260608-001",
        "interchange_control_id": "000001237",
        "interchange_receiver_id": "WALMART",
        "interchange_sender_id": "HUHTAMAKI",
        "invoice_date": "2026-06-08",
        "invoice_number": "INV-20260608-001",
        "order_number": "SO-20260608-001",
        "payment_terms": "NET30",
        "po_number": "4500012345",
        "ship_date": "2026-06-07",
        "total_amount": "6250.00",
        "vendor_code": "HUH-VENDOR-001"
    },
    "ob_810_notes": {
        "batch": "BATCH-INV-20260608-001",
        "global_unique_id": "EDI-810-20260608-001",
        "invoice_number": "INV-20260608-001",
        "note_text": "Thank you for your business",
        "note_type": "GEN"
    },
    "ob_810_sacdetails": {
        "allowance_charge_code": "C",
        "batch": "BATCH-INV-20260608-001",
        "description": "Fuel Surcharge",
        "global_unique_id": "EDI-810-20260608-001",
        "invoice_number": "INV-20260608-001",
        "line_number": "1",
        "method_of_handling": "06",
        "percent": "5.00",
        "sac_amount": "312.50"
    },
    "ob_810_sacheader": {
        "allowance_charge_code": "C",
        "batch": "BATCH-INV-20260608-001",
        "description": "Freight Charge",
        "global_unique_id": "EDI-810-20260608-001",
        "invoice_number": "INV-20260608-001",
        "method_of_handling": "06",
        "sac_amount": "150.00"
    },
    "ob_810_shipment": {
        "batch": "BATCH-INV-20260608-001",
        "bill_of_lading": "BOL-OB-001",
        "carrier_code": "RYDER",
        "global_unique_id": "EDI-810-20260608-001",
        "invoice_number": "INV-20260608-001",
        "ship_date": "2026-06-07",
        "shipment_id": "SHIP-20260607-001",
        "tracking_number": "RYDER-TRK-001",
        "weight": "5000",
        "weight_uom": "LB"
    },
    "ob_855": {
        "asn_number": "ASN-20260608-001",
        "global_unique_id": "EDI-855-20260608-001",
        "interchange_control_id": "000001238",
        "interchange_receiver_id": "WALMART",
        "interchange_sender_id": "HUHTAMAKI",
        "invoice_number": "INV-20260608-001",
        "order_number": "SO-20260608-001",
        "po_number": "4500012345",
        "status": "SENT"
    },
    "ob_855_po": {
        "acknowledgement_type": "AC",
        "global_unique_id": "EDI-855-20260608-001",
        "interchange_control_id": "000001238",
        "item_number": "HUH-ITEM-001",
        "line_number": "1",
        "order_number": "SO-20260608-001",
        "po_number": "4500012345",
        "promised_ship_date": "2026-06-09",
        "quantity_acknowledged": "500",
        "quantity_uom": "CA"
    },
    "ob_856": {
        "batch": "BATCH-ASN-20260608-001",
        "direction": "OB",
        "global_unique_id": "EDI-856-20260608-001",
        "interchange_control_id": "000001239",
        "interchange_receiver_id": "WALMART",
        "interchange_sender_id": "HUHTAMAKI",
        "order_number": "SO-20260608-001",
        "po_number": "4500012345",
        "shipment_id": "SHIP-20260607-001",
        "status": "SENT"
    },
    "ob_856_adr": {
        "address1": "702 SW 8th St",
        "address2": "",
        "address_type": "ST",
        "city": "Bentonville",
        "country": "US",
        "global_unique_id": "EDI-856-20260608-001",
        "name": "Walmart DC 6094",
        "state": "AR",
        "zip": "72716"
    },
    "ob_856_item": {
        "case_upc_14_digit": "10012345678905",
        "global_unique_id": "EDI-856-20260608-001",
        "item_description": "Molded Fiber Plate 10in",
        "item_number": "HUH-ITEM-001",
        "line_number": "1",
        "lot_number": "LOT-2026060801",
        "order_line_number": "1",
        "order_number": "SO-20260608-001",
        "po_number": "4500012345",
        "quantity_shipped": "500",
        "quantity_uom": "CA",
        "unit_price": "12.50"
    },
    "ob_856_order": {
        "global_unique_id": "EDI-856-20260608-001",
        "order_date": "2026-06-08",
        "order_number": "SO-20260608-001",
        "po_number": "4500012345",
        "shipment_id": "SHIP-20260607-001"
    },
    "ob_856_pkg": {
        "global_unique_id": "EDI-856-20260608-001",
        "item_number": "HUH-ITEM-001",
        "lot_number": "LOT-2026060801",
        "package_level": "P",
        "package_type": "PLT",
        "quantity_per_pack": "50",
        "sscc": "00612345678901234560"
    },
    "ob_856_shipmt": {
        "appointment_number": "APPT-001",
        "date_tbd1": "2026-06-09",
        "date_tbd2": "",
        "date_tbd3": "",
        "delivery_date": "2026-06-10",
        "department_number": "DEPT-001",
        "direction": "OB",
        "global_unique_id": "EDI-856-20260608-001",
        "interchange_control_id": "000001239",
        "interchange_receiver_id": "WALMART",
        "interchange_sender_id": "HUHTAMAKI",
        "load_number": "LOAD-001",
        "pro_number": "PRO-20260607-001",
        "seal_number": "SEAL-001",
        "ship_date": "2026-06-07",
        "shipment_id": "SHIP-20260607-001",
        "trailer_number": "TRL-001",
        "weight": "5000",
        "weight_uom": "LB"
    }
}

for name, data in samples_edi.items():
    path = f"samples/HUH_edi/{name}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  wrote {path}")

# ── HUH_ipc ──────────────────────────────────────────────────────────────────

samples_ipc = {
    "errors_fallback": {
        "created_date": TS,
        "error_msg": "ORA-01403: No data found. Integration FALLBACK failed to locate source record for PO 4500012345.",
        "po_number": "4500012345",
        "record_key": "FALLBACK-ERR-001",
        "status": "ERROR"
    },
    "errors_int1414": {
        "created_date": TS,
        "error_msg": "SAP IDOC posting failed: Material 1000001 not found in plant NA01.",
        "po_number": "4500012346",
        "record_key": "INT1414-ERR-001",
        "status": "ERROR"
    },
    "errors_int1417": {
        "created_date": TS,
        "error_msg": "ORA-20001: Order 20260608001 already processed.",
        "po_number": "4500099  ",
        "record_key": 1417001,
        "status": "DUPLICATE"
    },
    "errors_int4009": {
        "created_date": TS,
        "error_msg": "Connection timeout reaching Manhattan WMS endpoint after 30s. Retry 3/3 failed.",
        "po_number": "4500012348",
        "record_key": "INT4009-ERR-001",
        "status": "TIMEOUT"
    },
    "errors_int4072": {
        "created_date": TS,
        "error_msg": "EDI 856 ASN rejected: SCAC code 'XYZZ' not found in carrier master.",
        "po_number": "4500012349",
        "record_key": "INT4072-ERR-001",
        "status": "REJECTED"
    },
    "obruns": {
        "difference": 2,
        "fail_runs": 2,
        "integration_code": "HUH_OB_856",
        "integration_name": "HUH OB ASN to Walmart 856",
        "rice_object": "I",
        "success_percentage": 96.0,
        "success_runs": 48,
        "total_runs": 50
    },
    "recon": {
        "diffrence": 3,
        "fail_records": 3,
        "integration_code": "HUH_OB_810",
        "integration_name": "HUH OB Invoice to Walmart 810",
        "rice_object": "I",
        "success_percentage": 97.0,
        "success_records": 97,
        "total_records": 100
    }
}

for name, data in samples_ipc.items():
    path = f"samples/HUH_ipc/{name}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  wrote {path}")

# ── HUH_INTG_Search ──────────────────────────────────────────────────────────

samples_intg = {
    "Details": {
        "items": [
            {
                "action_request_id": 100123,
                "actual_delivery_date": "2026-06-10",
                "assign_status": "ASSIGNED",
                "business_unit": "NA",
                "carrier": "RYDER",
                "carrier_name": "Ryder Transportation",
                "created_by": "OIC_INTG",
                "creation_date": TS,
                "cube_uom": "CF",
                "cube_value": "480.5",
                "delivery_date": "2026-06-10",
                "delivery_date_utc": "2026-06-10",
                "delivery_time": "14:00",
                "delivery_time_utc": "19:00",
                "departure_date": "2026-06-09",
                "departure_date_utc": "2026-06-09",
                "departure_time": "06:00",
                "departure_time_utc": "11:00",
                "destination_city": "Chicago",
                "destination_name": "Walmart DC 6094",
                "destination_state": "IL",
                "destination_zip": "60601",
                "distance_uom": "MI",
                "erp_order_type": "SO",
                "file_header_id": 5001,
                "flatrate": 0,
                "freight_multiplier": 1.05,
                "fulfillmentorg_code": "M1",
                "handing_uom": "PLT",
                "handling_unit": "10",
                "integration_code": "HUH_TMS_204",
                "integration_run_id": 9001,
                "intentionally_blank": "",
                "int_message": "SUCCESS",
                "is_freight_flat": "N",
                "item_description": "Molded Fiber Plate 10in",
                "item_no": "HUH-ITEM-001",
                "last_reason": "",
                "line_haul_rate": "2.85",
                "line_no": "1",
                "load_plan_no": "LP-20260608-001",
                "load_status": "DISPATCHED",
                "load_weight": "5000",
                "ltl_class": "85",
                "means_of_transportation": "TL",
                "order_no": "SO-20260608-001",
                "order_type": "SO",
                "originating_city": "Green Bay",
                "originating_state": "WI",
                "originating_zip": "54301",
                "payment_method": "PREPAID",
                "pick_up_date": "2026-06-09",
                "pick_up_date_utc": "2026-06-09",
                "pick_up_time": "06:00",
                "pick_up_time_utc": "11:00",
                "pro_no": "PRO-20260607-001",
                "quantity": "500",
                "quantity_uom": "CA",
                "shipment_status": "IN_TRANSIT",
                "shipping_charge": "1425.00",
                "ship_line_num": "1",
                "ship_num": "SHIP-20260607-001",
                "site_id": "GB01",
                "source_transaction_id": "SO-20260608-001",
                "source_transaction_system": "ERP",
                "so_freight_status": "SENT",
                "so_header_id": 200456,
                "so_release_status": "RELEASED",
                "so_submit_status": "SUBMITTED",
                "so_update_status": "UPDATED",
                "stop_no": "1",
                "sub_inventory": "FG",
                "time_stamp": TS,
                "total_cost": "1425.00",
                "total_distance": "210",
                "to_number": "CUST-001",
                "trailer_number": "TRL-001",
                "transactioncategorycode": "OUTBOUND",
                "warehouse": "GB01",
                "weight_uom": "LB"
            }
        ]
    },
    "HUH_INTG_Search": {
        "items": [
            {
                "assign_status": "ASSIGNED",
                "erp_order_type": "SO",
                "file_id": 5001,
                "file_name": "RYDER_LP_20260608_001.txt",
                "integration_run_id": 9001,
                "int_messages": "SUCCESS",
                "load_plan_count_per_file": 1,
                "load_plan_no": "LP-20260608-001",
                "order_nos": "SO-20260608-001",
                "shipment_status": "IN_TRANSIT",
                "so_freight_status": "SENT",
                "so_release_status": "RELEASED",
                "so_submit_status": "SUBMITTED",
                "so_update_status": "UPDATED",
                "total_count": 1,
                "unique_id": "AAABcDEFGHIJKLM"
            }
        ]
    },
    "RyderLoadPlanData": {
        "items": [
            {
                "delivery_date": "2026-06-10",
                "delivery_time": "14:00",
                "departure_date": "2026-06-09",
                "departure_time": "06:00",
                "file_header_id": 5001,
                "integration_run_id": 9001,
                "load_plan_no": "LP-20260608-001",
                "order_no": "SO-20260608-001",
                "pick_up_date": "2026-06-09",
                "pick_up_time": "06:00"
            }
        ]
    },
    "ShipmentHeaderSearch": {
        "items": [
            {
                "carrier": "RYDER",
                "create_at": "Y",
                "int_run_id": 9001,
                "load_number": "LOAD-001",
                "number_of_chep_pallets": "2",
                "number_of_std_pallets": "8",
                "order_number": "SO-20260608-001",
                "org_code": "M1",
                "seal_number": "SEAL-001",
                "shipment": "SHIP-20260607-001",
                "ship_date": "2026-06-07",
                "source": "ERP",
                "status": "CONFIRMED",
                "total_count": 1,
                "trailer_number": "TRL-001",
                "transaction_date": "2026-06-07",
                "ucc_128_vase_pallet_code": "00612345678901234560"
            }
        ]
    },
    "ShipmentLineSearch": {
        "items": [
            {
                "error_dtl": "",
                "item": "HUH-ITEM-001",
                "licence_plate_number": "LPN-001",
                "locator": "A-01-01",
                "lot_number": "LOT-2026060801",
                "order_line_num": "1",
                "order_num": "SO-20260608-001",
                "over_under_ship_reason": "",
                "pro": "PRO-20260607-001",
                "requested_uom_code": "CA",
                "secondary_uom_code": "EA",
                "shipment": "SHIP-20260607-001",
                "shipment_method": "TL",
                "shipped_qty": 500,
                "ship_line_number": "1",
                "source": "ERP",
                "split_lpn_number": "",
                "status": "CONFIRMED",
                "subinv": "FG"
            }
        ]
    },
    "ShipmentSearch": {
        "items": [
            {
                "actual_ship_date": "2026-06-07",
                "actual_ship_time": "08:30",
                "carrier": "RYDER",
                "chep_pallet_count": "2",
                "created_at": TS,
                "err_msg": "",
                "int_run_id": 9001,
                "item": "HUH-ITEM-001",
                "load_number": "LOAD-001",
                "locator": "A-01-01",
                "lot_number": "LOT-2026060801",
                "number_of_std_pallets": "8",
                "order_line_num": "1",
                "order_number": "SO-20260608-001",
                "org_code": "M1",
                "original_lpn_number": "LPN-001",
                "pro": "PRO-20260607-001",
                "requested_uom_code": "CA",
                "seal_number": "SEAL-001",
                "secondary_uom_code": "EA",
                "shipment": "SHIP-20260607-001",
                "shipment_line_num": "1",
                "shipment_method": "TL",
                "shipped_qty": 500,
                "ship_date": "2026-06-07",
                "ship_time": "08:30",
                "source_system": "ERP",
                "split_lpn_number": "",
                "status": "CONFIRMED",
                "sub_inventory": "FG",
                "total_count": 1,
                "trailer_number": "TRL-001",
                "ucc_128_vase_pallet_code": "00612345678901234560"
            }
        ]
    },
    "ShipmentStatuses": {
        "items": [
            {"status": "PENDING"},
            {"status": "CONFIRMED"},
            {"status": "IN_TRANSIT"},
            {"status": "DELIVERED"},
            {"status": "ERROR"}
        ]
    },
    "TMSHeaderLineSearch": {
        "items": [
            {
                "attribute1": "",
                "carrier": "RYDER",
                "creation_date": DATE,
                "erp_dest_org_code": "WM-DC-6094",
                "erp_from_org_code": "M1",
                "error_message": "",
                "file_name": "RYDER_TMS_20260608_001.txt",
                "group_id": "GRP-001",
                "integration_run_id": 9001,
                "item": "HUH-ITEM-001",
                "last_update_date": DATE,
                "line_number": "1",
                "load_number": "LOAD-001",
                "lot_number": "LOT-2026060801",
                "lot_num_lotcontrol": "Y",
                "lpn": "LPN-001",
                "oic_instance_id": "OIC-PROD3-001",
                "order_code": "SO",
                "order_number": "SO-20260608-001",
                "quantity": "500",
                "receipt_date": "2026-06-10",
                "receipt_number": "RCV-001",
                "record_id": 10001,
                "remaining_qty": 0,
                "status": "PROCESSED",
                "total_count": 1,
                "vendor_name": "Huhtamaki Americas",
                "warehouse_code": "GB01"
            }
        ]
    },
    "TMSHeaderSearch": {
        "items": [
            {
                "carrier": "RYDER",
                "error_messages": "",
                "file_id": 5001,
                "file_name": "RYDER_TMS_20260608_001.txt",
                "integration_run_id": 9001,
                "load_number": "LOAD-001",
                "oic_instance_id": "OIC-PROD3-001",
                "receipt_date": "2026-06-10",
                "status": "PROCESSED",
                "total_count": 1,
                "total_quantity": 500,
                "vendor_name": "Huhtamaki Americas",
                "warehouse_code": "GB01"
            }
        ]
    },
    "TMSLineSearch": {
        "items": [
            {
                "carrier": "RYDER",
                "error_message": "",
                "item": "HUH-ITEM-001",
                "load_number": "LOAD-001",
                "lot_number": "LOT-2026060801",
                "lpn": "LPN-001",
                "order_code": "SO",
                "quantity": "500",
                "receipt_date": "2026-06-10",
                "record_id": 10001,
                "warehouse_code": "GB01"
            }
        ]
    },
    "TMSStatuses": {
        "items": [
            {"status": "PENDING"},
            {"status": "PROCESSED"},
            {"status": "ERROR"},
            {"status": "REPROCESSED"}
        ]
    }
}

for name, data in samples_intg.items():
    path = f"samples/HUH_INTG_Search/{name}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  wrote {path}")

print("\nDone.")
