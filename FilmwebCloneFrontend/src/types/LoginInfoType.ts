import type { GenderType } from "./GenderType"
import type { UserAccountType } from "./UserAccountType"
import type { UserRoleType } from "./UserRoleType"

export type LoginInfoType = {
    userId: number,
    firstName: string,
    lastName: string,
    email: string,
    gender?: GenderType,
    role: UserRoleType,
    accountType: UserAccountType
}