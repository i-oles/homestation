def toggle_single_bulb(self, params: domain.ToggleSingleParams) -> domain.BulbSettings:
    bulb_model = self.repo.get_bulb(params.ip)

    if bulb_model is None:
        raise Exception(f"could not find bulb with ip: {params.ip}")

    validate_bulb_state(bulb_model.active, params.is_active)

    if params.is_active:
        if params.luminance != bulb_model.luminance:
            bulb = Bulb(params.ip, effect="smooth")

            bulb.toggle()
            bulb.turn_off()

            self.repo.update_bulb_state(False, params.ip)
            self.repo.update_bulb_luminance(params.luminance, params.ip)

            return domain.BulbSettings(
                ip=params.ip,
                is_active=False,
                luminance=params.luminance,
            )

        bulb = Bulb(bulb_model.ip, effect="smooth")
        bulb.set_brightness(params.luminance)

        self.repo.update_bulb_luminance(params.luminance, params.ip)

        return domain.BulbSettings(
            ip=params.ip,
            is_active=True,
            luminance=params.luminance,
        )

    bulb = Bulb(params.ip, effect="smooth")
    bulb.set_brightness(params.luminance)
    bulb.turn_on()

    self.repo.update_bulb_state(True, params.ip)

    return domain.BulbSettings(
        ip=params.ip,
        is_active=True,
        luminance=bulb_model.luminance,
    )


def get_all_ips(self) -> list[str]:
    bulb = Query()
    bulb_data = self.db.search(bulb.active is True)

    if not bulb_data:
        raise Exception("Could not found any bulb")

    ips = []

    for bulb in bulb_data:
        ip = bulb.get("ip")
        if ip is "":
            raise Exception(f"Could not found any ip for bulb: {bulb}")

        ips.append(ip)

    return ips

